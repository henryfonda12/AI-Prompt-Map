import json,re,sys
with open(sys.argv[1],encoding='utf-8') as f:t=f.read()
with open(sys.argv[2],encoding='utf-8') as f:data=json.load(f)
# template and data must agree: every block on exactly one island, every section the template uses present
errors=[]
isles=re.search(r'const ISLES=\[(.*?)\n\];',t,re.S).group(1)
inisle=[int(n) for m in re.findall(r'blocks:\[([\d,\s]*)\]',isles) for n in m.split(',') if n.strip()]
nums=[b['n'] for b in data['blocks']]
errors+=[f'block {n} is not on any island: add it to ISLES in src/template.html' for n in nums if n not in inisle]
errors+=[f'ISLES lists block {n}, which is not in the source' for n in inisle if n not in nums]
errors+=[f'block {n} appears in ISLES more than once' for n in set(inisle) if inisle.count(n)>1]
errors+=[f'the source has no “## {k}” section, but the template uses it' for k in sorted(set(re.findall(r"D\.extra\['([^']+)'\]",t))) if k not in data['extra']]
if errors:
  print(f'ERRORS ({len(errors)}), page not built:',*errors,sep='\n  ',file=sys.stderr);sys.exit(1)
# escape every “<” so no source text can close or reopen the <script>
d=json.dumps(data,ensure_ascii=False).replace('<','\\u003c')
with open(sys.argv[3],'w',encoding='utf-8') as f:f.write(t.replace('__DATA__',d))
