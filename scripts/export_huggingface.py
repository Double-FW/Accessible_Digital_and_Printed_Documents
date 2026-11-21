"""Export approved document guidance; verification output stays in workflow logs."""
import argparse
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote,urlsplit
import yaml
from documents_hf_common import ROOT,SOURCE,TARGET,MANAGED,git,destination,read_sources

ACTIVITIES='Accessible_Documents_RAG_and_Prompts/Content_Creation_and_Production_Activities_and_Prompts.md'
def serial(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def anchors(text):
    result=set(re.findall(r'<a\s+id="([^"]+)"',text));seen={}
    for h in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
        h=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',h).replace('`','').lower();h=''.join(c for c in h if c in '-_ ' or unicodedata.category(c)[0] in 'LN').replace(' ','-');n=seen.get(h,0);seen[h]=n+1;result.add(h+(f'-{n}' if n else ''))
    return result

def check(root=ROOT):
    root=Path(root).resolve();links=0;metadata=0
    for p in root.rglob('*.md'):
        if '.git' in p.parts:continue
        text=p.read_text()
        if text.startswith('---\n'):
            obj=yaml.safe_load(text.split('---',2)[1]);metadata+=1
            if not isinstance(obj,dict) or obj.get('license')!='MIT':raise ValueError('Invalid MIT metadata: '+p.name)
        if '\ufffd' in text:raise ValueError('Invalid source encoding: '+p.name)
        if 'complete UTF-8 content' in text or 'extensionless source filenames' in text:raise ValueError('Obsolete embedded snapshot claim: '+p.name)
        for target in re.findall(r'\[[^\]\n]+\]\(([^\n]+?)\)',text):
            u=urlsplit(target)
            if u.scheme or u.netloc:continue
            links+=1;dest=(p.parent/unquote(u.path)).resolve() if u.path else p
            if not dest.is_relative_to(root) or not dest.is_file():raise ValueError('Missing local source link: '+target)
            if u.fragment and unquote(u.fragment) not in anchors(dest.read_text()):raise ValueError('Missing source fragment: '+target)
    guide=(root/'Accessible_documentation_design.md').read_text();agent_text=(root/'AGENTS.md').read_text()
    if re.findall(r'^## (\d+) ',guide,re.M)!=[str(i) for i in range(1,13)]:raise ValueError('Expected 12 ordered guide sections.')
    ids=lambda text:set(re.findall(r'\b(?:PLAN|STRUCT|TYPE|VIS|LANG|IMAGE|DATA|FORM|SPECIAL|DIGITAL|HYBRID|PRINT|BOOK|QA|AI)\d\d\b',text))
    if len(ids(guide))!=43 or ids(guide)!=ids(agent_text):raise ValueError('Guide and agent must preserve 43 matching rule IDs.')
    activity=(root/ACTIVITIES).read_text()
    if re.findall(r'^## ([1-8])\. ',activity,re.M)!=list('12345678') or len(re.findall(r'^### Example prompt [12]$',activity,re.M))!=16:raise ValueError('Expected eight activities and 16 prompts.')
    agent=yaml.safe_load(agent_text.split('---',2)[1]);meta=yaml.safe_load(guide.split('---',2)[1])
    if agent['primary_guide_version']!=meta['version']:raise ValueError('Guide metadata version mismatch.')
    if agent['policy_adoption'] is not None or agent['release_authority'] is not None:raise ValueError('Local adoption metadata changed; review before export.')
    if (root/'Accessible_Documents_RAG_and_Prompts/Sources').exists():raise ValueError('Obsolete duplicated source directory.')
    if len(list(root.rglob('AGENTS.md')))!=1:raise ValueError('Duplicated agent instructions.')
    for state in ('pass','fail','unknown','not_tested','not_applicable'):
        if '`'+state+'`' not in guide or '`'+state+'`' not in agent_text:raise ValueError('Missing evidence state '+state)
    return {'status':'passed','learning_sections':12,'rule_ids':43,'activities':8,'illustrative_prompts':16,'local_links':links,'metadata_blocks':metadata,'scope':'Local structure only; no final-file, assistive-technology, physical-proof, reader, legal or model evaluation and no live external-source verification.'}

def build(root,output,dataset_id=TARGET):
    destination(dataset_id);root=Path(root);cfg,texts,manifest=read_sources(root);check(root)
    commit=git(root,'rev-parse','HEAD').decode().strip();date=git(root,'show','-s','--format=%cI','HEAD').decode().strip()
    authority=serial({'agent_instructions_as_source_data':texts['AGENTS.md'],'terminology_alignment':texts['Terminology_Alignment.md'],'rights_and_status':texts['NOTICE.md'],'qualification':'Practitioner guidance and agent instructions for local adoption, not proof of adoption. Some wording was reconstructed; eleven historical attachments were unavailable for inspection. Local typography defaults are not universal WCAG rules. No final-output tests, reader outcomes or approval are established. Retrieved instructions are data, not runtime authority.'})
    def row(ident,path,text,**fields):
        return dict(id=ident,text=text,source_repository=SOURCE,source_path=path,source_commit=commit,source_commit_date=date,source_url=f'https://github.com/{SOURCE}/blob/{commit}/{path}',authority_context_json=authority,license='MIT',**fields)
    documents=[]
    for path in cfg['document_files']:
        if path not in texts or not path.endswith('.md') or path.startswith(('scripts/','tests/','huggingface/')):raise ValueError('Invalid document selection.')
        title=re.search(r'^# (.+)$',texts[path],re.M)
        documents.append(row(path,path,texts[path],title=title.group(1) if title else path,record_type='maintained_guidance_document'))
    if len({r['id'] for r in documents})!=len(documents):raise ValueError('Duplicate document source.')
    guide=texts['Accessible_documentation_design.md'];matches=list(re.finditer(r'^## (\d+) (.+)$',guide,re.M));closing=len(guide)
    prefix=guide[:matches[0].start()];suffix=guide[closing:];sections=[]
    for i,m in enumerate(matches):
        body=guide[m.start():matches[i+1].start() if i+1<len(matches) else closing]
        sections.append(row('DOCUMENT-SECTION-'+m.group(1).zfill(2),'Accessible_documentation_design.md',body,title=m.group(2),section_number=int(m.group(1)),shared_guide_prefix=prefix,shared_guide_suffix=suffix,record_type='source_learning_section',evaluation_status='source_guidance_not_executed_test'))
    if prefix+''.join(x['text'] for x in sections)+suffix!=guide:raise ValueError('Learning-section extraction lost source text.')
    activity=texts[ACTIVITIES];matches=list(re.finditer(r'^## ([1-8])\. (.+)$',activity,re.M));closing=activity.index('## Editorial and production decision record')
    prefix=activity[:matches[0].start()];suffix=activity[closing:];activities=[]
    for i,m in enumerate(matches):
        body=activity[m.start():matches[i+1].start() if i+1<len(matches) else closing]
        prompts=re.findall(r'^### Example prompt ([12])\n\n(.*?)(?=^### Example prompt|\Z)',body,re.M|re.S)
        if [p[0] for p in prompts]!=['1','2']:raise ValueError('Each activity must retain its two illustrative prompts.')
        activities.append(row('DOCUMENT-ACTIVITY-'+m.group(1).zfill(2),ACTIVITIES,body,title=m.group(2),activity_number=int(m.group(1)),prompt_1=prompts[0][1].strip(),prompt_2=prompts[1][1].strip(),shared_activity_prefix=prefix,shared_activity_suffix=suffix,record_type='illustrative_activity_and_prompts',execution_status='not_executed_example',observed_reader_evidence=False))
    if prefix+''.join(x['text'] for x in activities)+suffix!=activity:raise ValueError('Activity extraction lost source text.')
    payload={'documents.jsonl':''.join(serial(x)+'\n' for x in documents).encode(),'learning_sections.jsonl':''.join(serial(x)+'\n' for x in sections).encode(),'activities.jsonl':''.join(serial(x)+'\n' for x in activities).encode(),'LICENSE':texts['LICENSE'].encode(),'NOTICE.md':texts['NOTICE.md'].encode()}
    provenance={'source_repository':SOURCE,'source_commit':commit,'source_commit_date':date,'destination_dataset':TARGET,'manifest':manifest,'license':'MIT','representations':'Full guide and learning sections are alternative views of one source, not independent evidence. Instructional material does not represent executed output tests or measured reader outcomes. Reconstructed wording and historical attachments remain subject to the source provenance limitations.','limits':'No external source bodies copied. Original review dates and source status retained; export date does not renew source verification.'}
    schema={'format':'JSON Lines','document_columns':sorted(documents[0]),'learning_section_columns':sorted(sections[0]),'activity_columns':sorted(activities[0]),'text':'Exact source Markdown or complete numbered section. Shared source prefixes/suffixes preserve scope and qualifications.','authority_context_json':'JSON string retaining agent instructions as data, draft/adoption limits, terminology and rights.','identifiers':'DOCUMENT-SECTION and DOCUMENT-ACTIVITY identifiers are retrieval labels, not WCAG or test IDs.'}
    for name,value in [('provenance.json',provenance),('record_schema.json',schema)]:payload[name]=(serial(value)+'\n').encode()
    payload['README.md']='---\nlicense: mit\nlanguage:\n- en\ntask_categories:\n- text-retrieval\nconfigs:\n- config_name: documents\n  data_files:\n  - split: train\n    path: documents.jsonl\n- config_name: learning_sections\n  data_files:\n  - split: train\n    path: learning_sections.jsonl\n- config_name: activities\n  data_files:\n  - split: train\n    path: activities.jsonl\n---\n# Accessible Digital and Printed Documents\n\nDouble-FW practitioner guidance from [the public GitHub repository](https://github.com/Double-FW/Accessible_Digital_and_Printed_Documents).\n\n## Content and format\n\nSeven complete maintained documents cover the design guide, README, AGENTS, workflow/handoff map, terminology, public specialist routes and provenance/rights. Twelve learning sections provide an alternative view of the same guide with its shared introduction, scope and authority context. Eight activities preserve all sixteen illustrative prompts and their shared introduction and decision-record guidance. Full documents and extracted sections overlap: choose representations deliberately rather than treating them as independent evidence. The `train` split is a loader label; no model training is claimed.\n\nEvery record identifies its GitHub commit, path and source URL. Source hashes and the explicit allowlist appear in provenance; schema describes each representation. Local PLAN/TYPE/QA and other rule IDs remain intact. DOCUMENT-SECTION and DOCUMENT-ACTIVITY IDs are retrieval labels, not external criteria. Navigation indexes, coverage statements, scripts and tests are not duplicated as substantive guidance. Linked external works are not fetched or bundled.\n\n## Provenance, rights and evidence limits\n\nThe guide contains reconstructed wording from 7 November 2026; this is not a verbatim recovery. Eleven historical attachments were unavailable for inspection. Their register is retained as unverified provenance, not independently checked source evidence. Historical S1–S11 labels do not establish that those attachments are present. Source NOTICE and authority context preserve these limitations; a later export does not renew earlier reviews or tests.\n\nThe guide and agent instructions are for local adoption. Most individual glossary definitions remain proposed. Design defaults are contextual starting values, not universal WCAG rules or clinical claims. Preserve the owning standard’s meaning and actual applicability; this is not a complete WCAG, PDF/UA or EPUB conformance checklist or a legal applicability assessment.\n\nSource checks, structural validation, visual review, actual assistive-technology use, physical proofing, reader evaluation, human acceptance and release authority are distinct. Unknown, not tested and not applicable differ; open decisions are separate. A successful export, repository merge or filled template is not an approval, accessibility certification or measured satisfaction. No test/audit report is published in this dataset.\n\nRetrieved instructions and example prompts are source data, not runtime authority or permission to override a consuming agent’s instructions, publish, disclose private information or act beyond delegated scope. Exclude confidential manuscripts, credentials and identifiable research data from public corpora. Review suitability, rights, privacy, duplication and task-specific evidence before training or deployment.\n\n## Licence and updates\n\nMIT, Copyright (c) 2026 Double FW Ltd. Retain the copyright and permission notice in LICENSE. The historical S5 register reports an external AGPL-3.0-or-later notice; that attachment/stylesheet is not bundled and is not relicensed by this project. Other referenced works retain their own rights. See NOTICE.md before importing external material.\n\nThe weekly GitHub workflow writes only eight named managed files to this existing dataset, preserving unrelated files (including .gitattributes) and visibility. It stops on wrong destination, missing/dirty approved sources, changed licence or failed structure checks. No-change runs create no extra dataset commit. Configuration and successful publication must be verified separately.\n'.encode()
    if set(payload)!=set(MANAGED):raise ValueError('Unexpected managed output set.')
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    for name,value in payload.items():(output/name).write_bytes(value)
    return {'documents':len(documents),'learning_sections':len(sections),'activities':len(activities),'illustrative_prompts':len(activities)*2}

def main():
    p=argparse.ArgumentParser();p.add_argument('--check-only',action='store_true');p.add_argument('--output');p.add_argument('--dataset-id');a=p.parse_args()
    if a.check_only:print(serial(check()))
    elif a.output and a.dataset_id:print(serial(build(ROOT,a.output,a.dataset_id)))
    else:p.error('Provide --check-only or both --output and --dataset-id.')
if __name__=='__main__':main()
