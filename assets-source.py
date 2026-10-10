from pathlib import Path
import cairosvg
P=Path(__file__).resolve().parent/'assets'
ink='#263e59'
def ellipse(x,y,rx,ry,c):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}"/>'
def path(d,c='none',w=5):return f'<path d="{d}" fill="{c}" stroke="{ink}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def rect(x,y,w,h,c,r=10):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}"/>'
def face(x=150,y=100):return ellipse(x-17,y,3,4,ink)+ellipse(x+17,y,3,4,ink)+path(f'M{x-10} {y+17} Q{x} {y+22} {x+10} {y+17}',w=2)
def save(group,name,s):
 p=P/group;p.mkdir(parents=True,exist_ok=True)
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 300 300"><g stroke="{ink}" stroke-width="3" stroke-linejoin="round">{s}</g></svg>'
 cairosvg.svg2png(bytestring=svg.encode(),write_to=str(p/(name+'.png')))
for name,girl in [('pavel',False),('mila',True)]:
 skin='#f9cfaf';s=path('M119 216 L116 273 L139 273 L144 217','#527896')+path('M160 217 L164 273 L186 273 L182 216','#527896')
 s+=ellipse(123,277,22,9,'#304c67')+ellipse(179,277,22,9,'#304c67')
 s+=path('M105 140 Q89 160 83 207 Q87 222 100 211 L123 164',skin)+path('M194 141 Q211 165 216 207 Q211 224 200 210 L176 165',skin)
 s+=path('M119 128 Q150 116 182 128 L190 217 L109 217 Z','#ed8d8d' if girl else '#83c8ea')
 if girl:s+=ellipse(91,67,20,40,'#68483c')+ellipse(210,67,20,40,'#68483c')+ellipse(93,94,10,6,'#ef9696')+ellipse(207,94,10,6,'#ef9696')
 s+=ellipse(150,77,53,59,'#68483c')+ellipse(150,86,47,48,skin)+path('M105 69 Q120 17 157 34 Q193 23 198 69 Q174 60 164 46 Q143 69 105 69','#68483c',2)+face(150,88)
 save('heroes','hero-'+name,s)
for name,color,shirt in [('wolf','#a6afb9','#75c5c2'),('elephant','#b5bdc9','#f2cd70'),('horse','#b68363','#96bd8d')]:
 s=path('M185 200 Q270 157 251 247 Q237 270 196 232',color)
 s+=path('M114 214 L107 274 L139 274 L147 214',color)+path('M160 214 L162 274 L195 274 L185 213',color)+ellipse(123,279,24,10,'#586371')+ellipse(180,279,24,10,'#586371')
 s+=path('M110 137 Q84 157 80 207 Q80 222 96 216 L121 174',color)+path('M185 137 Q218 163 221 208 Q218 228 204 214 L177 171',color)+path('M117 128 Q150 120 182 128 L191 220 L108 220 Z',shirt)
 if name=='elephant':s+=ellipse(99,77,44,58,color)+ellipse(201,77,44,58,color)+ellipse(99,77,26,39,'#d9b8bd')+ellipse(201,77,26,39,'#d9b8bd')+ellipse(150,72,50,54,color)+face(150,66)+path('M133 87 L133 138 Q133 171 164 168 Q192 165 178 143 Q166 156 164 136 L166 88',color,3)
 elif name=='wolf':s+=path('M104 58 L104 14 L138 49','#a6afb9')+path('M164 49 L199 14 L197 66','#a6afb9')+ellipse(150,80,57,53,color)+ellipse(150,101,39,26,'#e6e4dc')+ellipse(150,91,13,9,ink)+face(150,72)
 else:s+=path('M113 57 L109 16 Q129 11 139 48',color)+path('M166 47 Q179 11 191 18 L191 64',color)+ellipse(152,85,49,65,color)+path('M125 43 Q162 12 178 43 L161 76 L147 61 L134 79 Z','#63483c')+ellipse(152,116,40,29,'#d1a580')+face(152,80)+ellipse(139,116,4,4,ink)+ellipse(165,116,4,4,ink)
 save('heroes','hero-'+name,s)
s=path('M176 222 Q262 239 269 146 Q285 49 225 31 Q175 10 177 76 Q181 99 211 87 Q242 116 203 157','#e8aa71')+ellipse(135,199,60,64,'#e8aa71')+ellipse(120,127,48,48,'#edb57d')+path('M84 96 L81 51 Q107 51 115 84','#e8aa71')+path('M130 84 Q151 49 165 55 L158 110','#e8aa71')+ellipse(119,144,27,21,'#ffdfb1')+face(120,119)+ellipse(78,254,35,12,'#e8aa71')+ellipse(150,255,38,12,'#e8aa71')+path('M87 182 Q62 195 74 217',w=4)
save('objects','object-squirrel',s)
s=rect(58,18,184,264,'#765044',16)
for x in [72,129,186]:
 for y in [31,91,151,211]:s+=rect(x,y,43,47,'#98654e',5)
save('objects','object-chocolate',s)
s=ellipse(150,153,134,133,'#f3c467')+ellipse(150,151,117,115,'#ffdb82')+ellipse(105,139,7,10,ink)+ellipse(195,139,7,10,ink)+ellipse(80,176,20,12,'#eda585')+ellipse(219,176,20,12,'#eda585')+path('M107 180 Q150 220 193 180',w=5)
save('objects','object-kolobok',s)
s=path('M16 120 Q150 53 284 120 L254 223 Q145 271 48 215 Z','#bb8b64')+ellipse(150,122,133,44,'#e7bc8a')+ellipse(150,124,109,28,'#8d6a55')+path('M51 161 Q150 202 260 163',w=4)+path('M69 199 Q150 230 243 199',w=3)
save('objects','object-boat',s)
s=path('M124 206 L114 263 L135 273 L150 208','#f7d3b5')+path('M168 206 L173 265 L195 269 L191 207','#f7d3b5')+ellipse(121,275,23,11,'#9b7cc0')+ellipse(188,276,24,11,'#9b7cc0')+path('M105 133 L55 186 L68 200 L124 163','#f7d3b5')+path('M192 135 L242 182 L229 201 L177 164','#f7d3b5')+path('M118 126 L181 126 L213 218 L87 218 Z','#b39bda')+ellipse(97,54,24,34,'#deac64')+ellipse(207,54,24,34,'#deac64')+ellipse(152,76,54,57,'#deac64')+ellipse(152,83,46,45,'#f7d3b5')+face(152,81)
for x,y in [(85,177),(217,176),(128,240),(182,241)]:s+=ellipse(x,y,9,9,'#eabb96')
s+=rect(121,151,61,14,'#ede2f7',7)
save('objects','object-doll',s)
for name in ['happy','sad','surprised','angry','sleepy']:
 s=ellipse(150,150,135,135,'#ffdb78')+ellipse(77,182,18,11,'#efb489')+ellipse(223,182,18,11,'#efb489')
 if name=='sleepy':s+=path('M91 134 Q105 153 119 134 M181 134 Q195 153 209 134',w=6)+path('M132 195 Q150 187 168 195',w=5)
 else:
  s+=ellipse(105,137,7,11,ink)+ellipse(195,137,7,11,ink)
  if name=='happy':s+=path('M106 185 Q150 237 194 185 Z','#fff6d8',4)
  if name=='sad':s+=path('M117 210 Q150 181 183 210 M86 112 L120 98 M180 98 L214 112',w=5)
  if name=='surprised':s+=ellipse(150,201,16,24,'#9e684e')+path('M87 103 Q104 84 121 103 M179 103 Q196 84 213 103',w=5)
  if name=='angry':s+=path('M85 103 L123 118 M177 118 L215 103 M119 210 Q150 191 181 210',w=5)
 save('moods','mood-'+name,s)
# Flat action symbols: only navy, orange and ivory, uniform rounded strokes.
orange='#f2a450';ivory='#fff4e3'
a={}
a['stroke']=path('M150 176 Q233 173 260 221 Q272 259 227 265 L92 265 Q54 265 55 231 Q62 201 96 190 L111 158 L132 184',ivory,9)+path('M61 85 L101 111 L150 122 L218 132 Q243 143 219 159 L155 155 L192 174 Q202 194 179 196 L120 173 L83 150 L40 142',orange,9)+path('M150 209 Q189 191 222 212',w=9)+ellipse(109,217,5,5,ink)
a['break']=path('M57 65 L141 88 L127 130 L143 150 L117 165 L100 205 L30 183 Z',orange,9)+path('M166 89 L242 65 L269 182 L195 207 L179 168 L158 149 L179 128 Z',orange,9)+path('M19 235 L47 172 Q57 156 73 170 L84 205 L112 219 L107 266 L46 282 Z',ivory,9)+path('M279 235 L253 172 Q242 156 227 171 L216 204 L188 220 L193 266 L254 282 Z',ivory,9)+path('M104 29 L88 48 M191 29 L210 48',w=9)
a['catch']=ellipse(150,78,53,53,orange)+path('M31 245 L29 186 L47 119 Q57 107 66 122 L62 166 L91 129 Q104 123 107 139 L88 180 L115 163 Q129 166 122 182 L99 216 L113 249 L79 275 Z',ivory,9)+path('M269 245 L271 186 L253 119 Q243 107 234 122 L238 166 L209 129 Q196 123 193 139 L212 180 L185 163 Q171 166 178 182 L201 216 L187 249 L221 275 Z',ivory,9)+path('M150 143 L150 198 M135 183 L150 201 L165 183',w=9)
a['push']=ellipse(66,45,25,25,ivory)+path('M69 84 L116 126 L159 129 M110 141 L157 153 M82 99 L61 177 L26 258 M61 177 L108 194 L100 264',w=14)+path('M165 169 L279 169 L257 230 L185 230 Z',orange,9)+path('M177 98 L268 98 M249 80 L270 98 L249 116',w=9)
a['put-to-bed']=path('M28 176 L28 271 M274 163 L274 271 M29 231 L274 231',w=10)+rect(37,177,228,50,ivory,8)+rect(205,168,53,32,ivory,8)+ellipse(192,148,24,24,orange)+path('M169 161 L105 176 L85 199 L164 205 L183 177 Z',orange,9)+path('M19 48 L73 60 L113 105 L158 130 Q171 147 151 150 L105 129 L62 94 L21 88',ivory,9)+path('M227 37 L227 106 M211 90 L227 110 L243 90',w=9)
for name,s in a.items():save('actions','action-'+name,s)
for name in ['game','cover']:
 s='<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><rect width="1920" height="1080" fill="#f9f6ed"/><path d="M0 0H1920V210Q1450 100 1000 210Q460 290 0 190Z" fill="#e6f3f5"/><path d="M0 945Q500 850 1000 960Q1500 1040 1920 925V1080H0Z" fill="#e4f0df"/>'
 for x,y,r in [(60,340,22),(1830,470,32),(1700,70,20),(190,900,20),(1720,930,16)]:s+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="#f2d58d"/>'
 if name=='cover':
  import base64
  for group,asset,x,y,w in [('heroes','hero-pavel',20,280,280),('heroes','hero-mila',1580,250,300),('heroes','hero-wolf',65,660,250),('heroes','hero-elephant',1510,700,260),('heroes','hero-horse',1680,520,230),('objects','object-kolobok',310,30,140),('objects','object-squirrel',1450,40,180),('objects','object-chocolate',40,80,140),('objects','object-boat',360,875,220),('objects','object-doll',1310,855,180)]:
   b=base64.b64encode((P/group/(asset+'.png')).read_bytes()).decode();s+=f'<image href="data:image/png;base64,{b}" x="{x}" y="{y}" width="{w}" height="{w}"/>'
 s+='</svg>';d=P/'backgrounds';d.mkdir(exist_ok=True);cairosvg.svg2png(bytestring=s.encode(),write_to=str(d/(name+'-background.png')))
