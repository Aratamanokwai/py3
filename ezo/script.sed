# -*- coding: utf-8 -*-
#
# # 較正の手引

# ## 使用方法
# ```sh
# $ sed -f script.sed text.txt
# ```
#
# ## 注意點
# テキストファイルは以下の樣式にする。
# 字文字符號: utf-8    改行符號: LF(unix)
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
# Ver.1.0   公開
# Ver.1.1   新字の單純舊字化（なんちやつて正字）に對應
# Ver.1.2   ハ行四段動詞に對應
# Ver.1.3   變換の追加
# Ver.1.4   辭書のスリム化
# Ver.1.5   舊字變換の追加
# Ver.1.7   R021216の變更

# ## 單純に正字に變換してはいけない語
#
# ### 「弁」の區別について
#
# べん	弁	かんむり、武弁・兵弁など
# べん	辨	わかち。わきまへ。あつかひ。辨當など。
# べん	辯	いひまはし。言葉遣。口先が巧みなこと。辯護など。
# べん	瓣	はなびら。なかご。機械のベン。花瓣など。
# べん	辦	なす、力を致すこと。そなふ、そなはる。合辦など。
# べん	辮	くむ。あむ。辮髮など。
#
# 「辧」は「辨」の異字體
# 「力」と「刀」を間違へないで下さい
#
# ### ヨオの扱ひについて
# #### 助動詞・間投詞・感動詞の場合は「よう」
# 「〜しヨオ」は「よう」（勉強しよう）
# 「俺々、俺だヨオ」は「よう」
# 「ヨオ、大統領」は「よう」
# #### ウ音便は單語次第
# 「お早う」は「はやい」だから「おはヤウ」
# 「住みヨオする」は「よく」だから「すみヨウする」
# 「酒に醉うて」は「ヱヒて」だから「さけにヱウて」
# （勿論、「酒に醉ふ」は「さけにヱフ」）
# #### 字音假名遣に就て
# 「要するに」は「エウするに」
# 「萬葉集」は「まんエフしふ」
# 「容器」は「ヨウき」
# 「指標」は「しヘウ」、發音は「シヒョオ」
# 「仕樣書」は「しヤウしよ」
# 「〜のヨオだ」も「樣」だから「ヤウ」
# ※　要するに、「ヨオ」を機械的に「やう」と變換しては駄目！
# 例、見やう見まねでやつて見うと思うたが、
#     これぢや、どうしやうも無いね。
# ### 蛇足
#  - 自稱の「余」は「餘」ではない。
#  - 自稱の「予」は「豫」ではない。
#  - 「強」は「强」でなくとも可い。「強」が正字。
#  - 「回」は「囘」でなくとも可い。「回」が正字で「囘」は古字。
#  - わけ 訣	譯（訳）は宛字で本來「わけ」の訓は無い

# # 新字/正字の對應
y/亜悪圧囲医為壱飲隠欝営栄衛駅円艶/亞惡壓圍醫爲壹飮隱鬱營榮衞驛圓艷/
y/塩奥応欧殴穏桜仮価画届会壊懐絵拡/鹽奧應歐毆穩櫻假價畫屆會壞懷繪擴/
y/覚学岳楽殻勧巻歓缶観関巌顔陥帰/覺學嶽樂殼勸卷歡罐觀關巖顏陷歸/
y/気亀偽戯犠旧拠挙峡挟狭暁区駆勲径/氣龜僞戲犧舊據擧峽挾狹曉區驅勳徑/
y/恵渓経継茎蛍軽鶏芸欠倹剣圏検権献/惠溪經繼莖螢輕鷄藝缺儉劍圈檢權獻/
y/県険顕験厳効広恒鉱号国済砕冊/縣險顯驗嚴效廣恆鑛號國濟碎册/
y/剤雑参蚕桟惨讃賛残歯辞湿実舎写/劑雜參蠶棧慘讚贊殘齒辭濕實舍寫/
y/釈寿収穐従渋獣縦粛処叙奨将焼称証/釋壽收龝從澁獸縱肅處敍奬將燒稱證/
y/乗剰壌嬢条浄畳穣譲醸触寝慎晋真尽/乘剩壤孃條淨疊穰讓釀觸寢愼晉眞盡/
y/縄図粋酔穂随髄数枢声静斉窃摂専戦/繩圖粹醉穗隨髓數樞聲靜齊竊攝專戰/
y/浅潜繊践銭禅壮双捜挿争総聡荘装騒/淺濳纖踐錢禪壯雙搜插爭總聰莊裝騷/
y/臓蔵属続堕体対帯滞台択沢単担胆団/臟藏屬續墮體對帶滯臺擇澤單擔膽團/
y/弾断遅痴昼虫鋳庁聴鎮逓鉄転点伝兎/彈斷遲癡晝蟲鑄廳聽鎭遞鐵轉點傳兔/
y/党当盗灯稲闘独読悩脳廃拝売麦発/黨當盜燈稻鬪獨讀惱腦廢拜賣麥發/
y/秘髪抜蛮浜払仏変並箆辺餅舗宝豊冒/祕髮拔蠻濱拂佛變竝篦邊餠舖寶豐冐/
y/没万満黙来乱弥薬訳予余与誉揺様謡/沒萬滿默來亂彌藥譯豫餘與譽搖樣謠/
y/覧両猟塁励礼霊齢恋炉労楼滝禄芦湾/覽兩獵壘勵禮靈齡戀爐勞樓瀧祿蘆灣/
y/嘱往嘩鈎券勅竪厨曽祢竜/囑徃譁鉤劵敕豎廚曾禰龍/

y/煙却娘糸携涛潅熙珱楕桧梼梹檪/烟卻孃絲攜濤灌煕瓔橢檜檮檳櫟/
y/亘卆聟枦渊尓畄翆軣鈬鼡禀竃筝緕/亙卒婿櫨淵爾留翠轟鐸鼠稟竈箏纃/
y/伜僣侭弯忰抬撹昿畴皐碍砿砺舮薮/倅僭儘彎悴擡攪曠疇皋礙礦礪艫藪/
y/鈩鑚陏隷覇虱蝿蛎褒諌弐賎迩隣頚/鑪鑽隋隸霸蝨蠅蠣襃諫貳賤邇鄰頸/
y/鰛鯵鴬鷏麸斎尭槙瑶遥児/鰮鰺鶯鷆麩齋堯槇瑤遙兒/
y/閙閧闘/鬧鬨鬪/

y/寛糾教郷薫群妊粘晩瓶萌郎/寬糺敎鄕薰羣姙黏晚甁萠郞/
y/黒冴緒床刃瀬清青跡潜窓横/黑冱緖牀刄瀨淸靑蹟潛窗橫/
y/翻麺欲頼略緑凛痩巣神増/飜麵慾賴畧綠凜瘦巢神增/

# 文字化け對策
y/〜/ー/g

# 機種依存文字
# y/涙/淚/

# ### 一覽
# s/新字/正字/g
# 但し、
# 必ずしも左側の新字表現を右側の正字表現に直せば可いといふものではない。
#
s/亞鈴/啞鈴/g
s/暗唱/暗誦/g
s/暗夜/闇夜/g
s/優俊/優駿/g
s/意向/意嚮/g
s/衣裝/衣裳/g
s/委縮/萎縮/g
s/一獲千金/一攫千金/g
s/陰影/陰翳/g
s/隱滅/湮滅/g
s/英才/穎才/g
s/英知/叡智/g
s/憶病/臆病/g
s/恩義/恩誼/g
s/耕運機/耕耘機/g
s/交歡/交驩/g
s/交差/交叉/g
s/更正/甦生/g
s/香典/香奠/g
s/高騰/昂騰/g
s/高揚/昂揚/g
s/效率/效率/g
s/講和/媾和/g
s/畫期的/劃期的/g
s/格鬪/挌鬪/g
s/格好/恰好/g
s/活發/活潑/g
s/格幅/恰幅/g
s/個條書/箇條書/g
s/干害/旱害/g
s/間缺/間歇/g
s/肝心/肝腎/g
s/關數/函數/g
s/干天/旱天/g
s/乾留/乾溜/g
s/合弁/合辦/g
s/舊蹟/舊蹟/g
s/糺明/糺明/g
s/氣炎/氣焔/g
s/飢餓/饑餓/g
s/喜々/嬉々/g
s/企畫/企劃/g
s/奇形/畸形/g
s/希元素/稀元素/g
s/希釋/稀釋/g
s/奇人/畸人/g
s/希少/稀少/g
s/棄損/毀損/g
s/希代/稀代/g
s/機知/機智/g
s/喫水/吃水/g
s/氣迫/氣魄/g
s/希薄/稀薄/g
s/奇弁/詭辯/g
s/危弁/詭辯/g
s/供宴/饗宴/g
s/強固/鞏固/g
s/橋頭保/橋頭堡/g
s/供應/饗應/g
s/喜遊曲/嬉遊曲/g
s/凶行/兇行/g
s/凶漢/兇漢/g
s/凶器/兇器/g
s/凶刄/兇刄/g
s/凶暴/兇暴/g
s/凶變/兇變/g
s/共役/共軛/g
s/據金/醵金/g
s/據出/醵出/g
s/希硫酸/稀硫酸/g
s/禁固/禁錮/g
s/均整/均齊/g
s/義援/義捐/g
s/御者/馭者/g
s/魚勞/魚撈/g
s/技量/伎倆/g
s/吟唱/吟誦/g
s/區畫/區劃/g
s/掘削/掘鑿/g
s/快活/快闊/g
s/回轉/廻轉/g
s/回覽/廻覽/g
s/回復/恢復/g
s/花弁/花瓣/g
s/回廊/囘游/g
s/鑛業/礦業/g
s/廣壯/宏壯/g
s/鑛石/礦石/g
s/廣大/宏大/g
s/廣範/廣汎/g
s/廣野/曠野/g
s/畫期的/劃期的/g
s/畫然/劃然/g
s/擴大/廓大/g     # 擴大でも可
s/管弦/管絃/g
s/歡待/款待/g     # 歡待も可
s/貫錄/貫祿/g
s/訓戒/訓誡/g
s/薰蒸/燻蒸/g
s/薰製/燻製/g
s/計畫/計劃/g
s/傾向/傾嚮/g
s/敬謙/敬虔/g
s/係爭/繋爭/g
s/係船/繋船/g
s/係屬/繋屬/g
s/係留/繋留/g
s/決壞/決潰/g
s/決起/蹶起/g
s/決別/訣別/g
s/肩甲骨/肩胛骨/g
s/弦樂/絃樂/g
s/險阻/嶮岨/g
s/建坪率/建蔽率/g
s/硏摩/硏磨/g
s/激高/激昂/g
s/下克上/下尅上/g
s/月食/月蝕/g
s/弦歌/絃歌/g
s/元凶/元兇/g
s/嚴然/儼然/g
s/幻惑/眩惑/g
s/拘引/勾引/g
s/控除/扣除/g
s/廣報/弘報/g
s/枯渴/涸渴/g
s/古希/古稀/g
s/骨格/骨骼/g
s/雇用/雇傭/g
s/混交/混淆/g
s/混然/渾然/g
s/根底/根柢/g
s/倉皇/蒼惶/g
s/相克/相剋/g
s/裝丁/裝釘/g
# さうめつ	剿滅	みなごろし
# さうめつ	掃滅	はらひのけほろぼすこと
s/削岩/鑿岩/g
s/酢酸/醋酸/g
s/贊仰/讚仰/g
s/三弦/三絃/g
s/三差/三叉/g
s/贊辭/讚辭/g
s/散水/撒水/g
s/贊美/讚美/g
s/散布/撒布/g
s/障害/障礙/g
s/象眼/象嵌/g
s/座視/坐視/g
s/座州/坐洲/g
s/座礁/坐礁/g
s/雜踏/雜沓/g
s/集荷/蒐荷/g
s/刺激/刺戟/g
s/死體/屍體/g
s/質草/質種/g
s/七轉八倒/七顚八倒/g
s/十戒/十誡/g
s/紫班/紫斑/g
s/死沒/死歿/g
s/車兩/車輌/g
s/終息/終熄/g
s/集落/聚落/g
s/俊才/駿才/g
s/俊足/駿足/g
s/俊馬/駿馬/g
s/稱贊/稱讚/g
s/賞贊/賞讚/g
s/昇敍/陞敍/g
s/食事療法/食餌療法/g
s/食盡/蝕甚/g
s/試練/試煉/g
s/侵食/侵蝕/g
s/浸食/浸蝕/g
s/針術/鍼術/g
s/眞蹟/眞蹟/g
s/伸長/伸暢/g
s/浸透/滲透/g
s/心拍/心搏/g
s/侵畧/侵掠/g
s/順化/馴化/g
s/順守/遵守/g
s/純朴/醇朴/g
s/蒸留/蒸溜/g
s/敍情/抒情/g
s/尋問/訊問/g
s/衰退/衰頽/g
s/消夏/銷夏/g
s/消卻/銷卻/g
s/植民/殖民/g
s/焦燥/焦躁/g
s/消沈/銷沈/g
s/勝利/捷利/g     # 勝利（しようり）のままでも可
s/先鋭/尖鋭/g
s/選考/銓衡/g
s/船倉/船艙/g
s/扇情/煽情/g
s/戰々恐々/戰々兢々/g
s/專斷/擅斷/g
s/扇動/煽動/g
s/先兵/尖兵/g
s/戰沒/戰歿/g
s/冗舌/饒舌/g
s/絕贊/絕讚/g
s/總合/綜合/g
s/總菜/惣菜/g
s/阻喪/沮喪/g
s/阻止/沮止/g
s/疎水/疏水/g
s/疎通/疏通/g
s/疎明/疏明/g
s/族生/簇生/g
s/粗末/麁末/g
s/退色/褪色/g
s/退勢/頽勢/g
s/臺頭/擡頭/g
s/退廢/頽廢/g
s/臺風/颱風/g
s/代弁/代辯/g
s/倒壞/倒潰/g
s/高根の花/高嶺の花/g
s/踏襲/蹈襲/g
s/炭鑛/炭礦/g
s/嘆願/歎願/g
s/端座/端坐/g
s/短編/短篇/g
s/奪畧/奪掠/g
s/暖房/煖房/g
s/暖爐/煖爐/g
s/抽選/抽籤/g
s/知能/智能/g
s/知謀/智謀/g
s/長編/長篇/g
s/注解/註解/g
s/注釋/註釋/g
s/注文/註文/g
s/沈殿/沈澱/g
s/丁重/鄭重/g
s/丁寧/叮嚀/g
s/停泊/碇泊/g
s/鳥觀/鳥瞰/g
s/鳥觀/鳥瞰/g
s/轉倒/顚倒/g
s/展轉/輾轉/g
s/轉覆/顚覆/g
s/條蟲/絛蟲/g
s/殿部/臀部/g
s/殿粉/澱粉/g
s/特集/特輯/g
s/途絕/杜絕/g
s/廢虛/廢墟/g
s/背徳/悖徳/g
s/配列/排列/g
s/放棄/抛棄/g
s/芳純/芳醇/g
s/包帶/繃帶/g
s/包丁/庖丁/g
s/放物線/抛物線/g
s/白亞/白堊/g
s/薄幸/薄倖/g
s/拍動/搏動/g
s/破碎/破摧/g
s/發酵/醗酵/g
s/波亂/波瀾/g
s/反旗/叛旗/g
s/反逆/叛逆/g
s/繁殖/蕃殖/g
s/班點/斑點/g
s/反發/反撥/g
s/反亂/叛亂/g
s/梅雨/黴雨/g
s/梅毒/黴毒/g
s/買弁/買辦/g
s/防壓/防遏/g
s/妨害/妨礙/g
s/防御/防禦/g
s/膨張/膨脹/g
s/暴露/曝露/g
s/拔粹/拔萃/g
s/蠻族/蕃族/g
s/飛語/蜚語/g
s/非才/菲才/g
s/披歷/披瀝/g
s/廣野/曠野/g
s/病沒/病歿/g
s/風光明美/風光明媚/g
s/風刺/諷刺/g
s/風諭/諷喩/g
s/腐食/腐蝕/g
s/普段/不斷/g
s/符丁/符牒/g
s/腐亂/腐爛/g
s/粉裝/扮裝/g
s/格好/恰好/g
s/分留/分溜/g
s/漂然/飄然/g
s/邊境/邊疆/g
s/編集/編輯/g
s/片頭痛/偏頭痛/g
s/弁護/辯護/g
s/弁當/辨當/g
s/偏平/扁平/g
s/弁髮/辮髮/g
s/保育/哺育/g
s/崩壞/崩潰/g
s/奉持/捧持/g
s/補佐/輔佐/g
s/舖裝/鋪裝/g
s/補導/輔導/g
s/保母/保姆/g
s/保壘/堡壘/g
s/母指/拇指/g
s/母印/拇印/g
s/盲想/妄想/g
s/盲執/妄執/g
s/盲動/妄動/g
s/盲念/妄念/g
s/摩耗/磨耗/g
s/摩滅/磨滅/g
s/脈拍/脈愽/g
s/無知/無智/g
s/名譽/名譽/g
s/綿花/棉花/g
s/模索/摸索/g
s/野卑/野鄙/g
s/友宜/友誼/g
s/裕然/悠然/g
s/油送船/油槽船/g
s/溶解/鎔解/g
s/溶岩/熔岩/g
s/溶接/熔接/g
s/世論/輿論/g
s/落後/落伍/g
s/落盤/落磐/g
s/亂掘/濫掘/g
s/亂作/濫作/g
s/亂造/濫造/g
s/亂讀/濫讀/g
s/亂發/濫發/g
s/亂費/濫費/g
s/亂用/濫用/g
s/留飮/溜飮/g
s/留出/溜出/g
s/里謠/俚謠/g
s/理屈/理窟/g
s/利口/悧口/g
s/理知/理智/g
s/離反/離叛/g
s/畧奪/掠奪/g
s/輪郭/輪廓/g
s/連係/連繋/g
s/練炭/煉炭/g
s/練乳/煉乳/g
s/連絡/聯絡/g
s/連盟/聯盟/g
s/連合/聯合/g
s/連邦/聯邦/g
s/慰謝料/慰藉料/g
s/回向/廻向/g
s/温暖/温煖/g
# ## 追加
s/榮養/營養/g
s/ホ乳/哺乳/g
s/ハ蟲/爬蟲/g
s/障害/障礙/g
s/障礙/障礙/g
s/礙子/礙子/g

##  注意點の指摘。
# ばうだい	厖大	形容動詞で、量や規模が大きいさま。
# ばうだい	膨大	サ變動詞で、膨れて大きくなること。
s/膨大な/厖大な/g
## 牆壁	かきとかべと
## 障壁	妨げとなるもののこと。「關稅―」
s/障壁/【牆壁|障壁】/g
## 情義	人情と義理のこと。
## 情誼	人とつきあふ上での人情や誠意のこと。
s/情義/【情誼|情義】/g
## 收集	寄せ集めること。「ごみの―」
## 蒐集	コレクション。「切手の−」
s/收集/【收集|蒐集】/g
## 壞亂	やぶれ亂れること
## 潰亂	ちりぢりに亂れること
s/壞亂/【壞亂|潰亂】/g
## 確乎	しつかりしてゐるさま（副詞）確乎として、確乎たる存在である。
## 確固	しつかりして固いこと（名詞）
s/確固と/確乎と/g
s/確固たる/確乎たる/g
# りかい	理解	内容、意味などが分かること。
# りくわい	理會	物事の道理を會得すること。
s/理解/【理解|理會】/g
# ## 御好み
# y/着/著/g   # 著は正字、着は行書體
# y/咲/笑/g   # 咲は笑の古字、漢文では同字
s/高進/【昂進|亢進】/g
s/興奮/【昂奮|亢奮】/g
s/技量/【伎倆|技倆】/g
s/火炎/【火炎|火焰】/g
s/恐喝/【脅喝|恐喝】/g
s/裝丁/【裝釘|裝幀】/g
s/制御/【制馭|制禦】/g
s/抵觸/【牴觸|觝觸】/g
s/敷延/【敷衍|布衍】/g
s/練摩/【練磨|鍊磨】/g
s/了見/【了簡|料簡】/g

# ## 差別用語対策
# s/中國/支那/g
# s/中共/支共/g
# s/親中/親支/g

# ## 正假名遣への變換
s/おり、/をり、/g
s/おりま/をりま/g
s/こういう/かういふ/g
s/こうした/かうした/g
s/そうした/さうした/g
s/てしまう/てしまふ/g
s/てしまい/てしまひ/g
s/ている/てゐる/g
s/ていた/てゐた/g
s/ていて/てゐて/g
s/ていない/てゐない/g
s/そういう/さういふ/g
s/するよう/するやう/g
s/できるよう/できるやう/g
s/やろう/やらう/g

# ## ハ行四段
s/いわ/いは/g
s/いい/い【い|ひ】/g
s/いう/いふ/g
s/いえ/いへ/g
s/いお/いは/g
s/いふた/いうた/g
s/いうため/いふため/g
s/いふて/いうて/g
s/笑わ/笑は/g
s/笑い/笑ひ/g
s/笑う/笑ふ/g
s/笑え/笑へ/g
s/笑お/笑は/g
s/笑ふた/笑うた/g
s/笑うため/笑ふため/g
s/笑ふて/笑うて/g
s/救わ/救は/g
s/救い/救ひ/g
s/救う/救ふ/g
s/救え/救へ/g
s/救お/救は/g
s/救ふた/救うた/g
s/救うため/救ふため/g
s/救ふて/救うて/g
s/障碍わ/障碍は/g
s/障碍い/障碍ひ/g
s/障碍う/障碍ふ/g
s/障碍え/障碍へ/g
s/障碍お/障碍は/g
s/障碍ふた/障碍うた/g
s/障碍うため/障碍ふため/g
s/障碍ふて/障碍うて/g
s/扱わ/扱は/g
s/扱い/扱ひ/g
s/扱う/扱ふ/g
s/扱え/扱へ/g
s/扱お/扱は/g
s/扱ふた/扱うた/g
s/扱うため/扱ふため/g
s/扱ふて/扱うて/g
s/慕わ/慕は/g
s/慕い/慕ひ/g
s/慕う/慕ふ/g
s/慕え/慕へ/g
s/慕お/慕は/g
s/慕ふた/慕うた/g
s/慕うため/慕ふため/g
s/慕ふて/慕うて/g
s/買わ/買は/g
s/買い/買ひ/g
s/買う/買ふ/g
s/買え/買へ/g
s/買お/買は/g
s/買ふた/買うた/g
s/買うため/買ふため/g
s/買ふて/買うて/g
s/飼わ/飼は/g
s/飼い/飼ひ/g
s/飼う/飼ふ/g
s/飼え/飼へ/g
s/飼お/飼は/g
s/飼ふた/飼うた/g
s/飼うため/飼ふため/g
s/飼ふて/飼うて/g
s/拂わ/拂は/g
s/拂い/拂ひ/g
s/拂う/拂ふ/g
s/拂え/拂へ/g
s/拂お/拂は/g
s/拂ふた/拂うた/g
s/拂うため/拂ふため/g
s/拂ふて/拂うて/g
s/問わ/問は/g
s/問い/問ひ/g
s/問う/問ふ/g
s/問え/問へ/g
s/問お/問は/g
s/問ふた/問うた/g
s/問うため/問ふため/g
s/問ふて/問うて/g
s/願わ/願は/g
s/願い/願ひ/g
s/願う/願ふ/g
s/願え/願へ/g
s/願お/願は/g
s/願ふた/願うた/g
s/願うため/願ふため/g
s/願ふて/願うて/g
s/謂わ/謂は/g
s/謂い/謂ひ/g
s/謂う/謂ふ/g
s/謂え/謂へ/g
s/謂お/謂は/g
s/謂ふた/謂うた/g
s/謂うため/謂ふため/g
s/謂ふて/謂うて/g
s/云わ/云は/g
s/云い/云ひ/g
s/云う/云ふ/g
s/云え/云へ/g
s/云お/云は/g
s/云ふた/云うた/g
s/云うため/云ふため/g
s/云ふて/云うて/g
s/言わ/言は/g
s/言い/言ひ/g
s/言う/言ふ/g
s/言え/言へ/g
s/言お/言は/g
s/言ふた/言うた/g
s/言うため/言ふため/g
s/言ふて/言うて/g
s/味わわ/味はは/g
s/味わい/味はひ/g
s/味わう/味はふ/g
s/味わえ/味はへ/g
s/味わお/味はは/g
s/味はふた/味はうた/g
s/味はうため/味はふため/g
s/味はふて/味はうて/g
s/誘わ/誘は/g
s/誘い/誘ひ/g
s/誘う/誘ふ/g
s/誘え/誘へ/g
s/誘お/誘は/g
s/誘ふた/誘うた/g
s/誘うため/誘ふため/g
s/誘ふて/誘うて/g
s/惑わ/惑は/g
s/惑い/惑ひ/g
s/惑う/惑ふ/g
s/惑え/惑へ/g
s/惑お/惑は/g
s/惑ふた/惑うた/g
s/惑うため/惑ふため/g
s/惑ふて/惑うて/g
s/通わ/通は/g
s/通い/通ひ/g
s/通う/通ふ/g
s/通え/通へ/g
s/通お/通は/g
s/通ふた/通うた/g
s/通うため/通ふため/g
s/通ふて/通うて/g
s/疑わ/疑は/g
s/疑い/疑ひ/g
s/疑う/疑ふ/g
s/疑え/疑へ/g
s/疑お/疑は/g
s/疑ふた/疑うた/g
s/疑うため/疑ふため/g
s/疑ふて/疑うて/g
s/違わ/違は/g
s/違い/違ひ/g
s/違う/違ふ/g
s/違え/違へ/g
s/違お/違は/g
s/違ふた/違うた/g
s/違うため/違ふため/g
s/違ふて/違うて/g
s/行わ/行は/g
s/行い/行ひ/g
s/行う/行ふ/g
s/行え/行へ/g
s/行お/行は/g
s/行ふた/行うた/g
s/行うため/行ふため/g
s/行ふて/行うて/g
s/襲わ/襲は/g
s/襲い/襲ひ/g
s/襲う/襲ふ/g
s/襲え/襲へ/g
s/襲お/襲は/g
s/襲ふた/襲うた/g
s/襲うため/襲ふため/g
s/襲ふて/襲うて/g
s/構わ/構は/g
s/構い/構ひ/g
s/構う/構ふ/g
s/構え/構へ/g
s/構お/構は/g
s/構ふた/構うた/g
s/構うため/構ふため/g
s/構ふて/構うて/g
s/負わ/負は/g
s/負い/負ひ/g
s/負う/負ふ/g
s/負え/負へ/g
s/負お/負は/g
s/負ふた/負うた/g
s/負うため/負ふため/g
s/負ふて/負うて/g
s/會わ/會は/g
s/會い/會ひ/g
s/會う/會ふ/g
s/會え/會へ/g
s/會お/會は/g
s/會ふた/會うた/g
s/會うため/會ふため/g
s/會ふて/會うて/g
s/合わ/合は/g
s/合い/合ひ/g
s/合う/合ふ/g
s/合え/合へ/g
s/合お/合は/g
s/合ふた/合うた/g
s/合うため/合ふため/g
s/合ふて/合うて/g
s/使わ/使は/g
s/使い/使ひ/g
s/使う/使ふ/g
s/使え/使へ/g
s/使お/使は/g
s/使ふた/使うた/g
s/使うため/使ふため/g
s/使ふて/使うて/g
s/想わ/想は/g
s/想い/想ひ/g
s/想う/想ふ/g
s/想え/想へ/g
s/想お/想は/g
s/想ふた/想うた/g
s/想うため/想ふため/g
s/想ふて/想うて/g
s/思わ/思は/g
s/思い/思ひ/g
s/思う/思ふ/g
s/思え/思へ/g
s/思お/思は/g
s/思ふた/思うた/g
s/思うため/思ふため/g
s/思ふて/思うて/g
s/念わ/念は/g
s/念い/念ひ/g
s/念う/念ふ/g
s/念え/念へ/g
s/念お/念は/g
s/念ふた/念うた/g
s/念うため/念ふため/g
s/念ふて/念うて/g
s/失わ/失は/g
s/失い/失ひ/g
s/失う/失ふ/g
s/失え/失へ/g
s/失お/失は/g
s/失ふた/失うた/g
s/失うため/失ふため/g
s/失ふて/失うて/g
s/逢わ/逢は/g
s/逢い/逢ひ/g
s/逢う/逢ふ/g
s/逢え/逢へ/g
s/逢お/逢は/g
s/逢ふた/逢うた/g
s/逢うため/逢ふため/g
s/逢ふて/逢うて/g
s/伺わ/伺は/g
s/伺い/伺ひ/g
s/伺う/伺ふ/g
s/伺え/伺へ/g
s/伺お/伺は/g
s/伺ふた/伺うた/g
s/伺うため/伺ふため/g
s/伺ふて/伺うて/g
s/吸わ/吸は/g
s/吸い/吸ひ/g
s/吸う/吸ふ/g
s/吸え/吸へ/g
s/吸お/吸は/g
s/吸ふた/吸うた/g
s/吸うため/吸ふため/g
s/吸ふて/吸うて/g
s/追わ/追は/g
s/追い/追ひ/g
s/追う/追ふ/g
s/追え/追へ/g
s/追お/追は/g
s/追ふた/追うた/g
s/追うため/追ふため/g
s/追ふて/追うて/g
s/舞わ/舞は/g
s/舞い/舞ひ/g
s/舞う/舞ふ/g
s/舞え/舞へ/g
s/舞お/舞は/g
s/舞ふた/舞うた/g
s/舞うため/舞ふため/g
s/舞ふて/舞うて/g
s/添わ/添は/g
s/添い/添ひ/g
s/添う/添ふ/g
s/添え/添へ/g
s/添お/添は/g
s/添ふた/添うた/g
s/添うため/添ふため/g
s/添ふて/添うて/g
s/給わ/給は/g
s/給い/給ひ/g
s/給う/給ふ/g
s/給え/給へ/g
s/給お/給は/g
s/給ふた/給うた/g
s/給うため/給ふため/g
s/給ふて/給うて/g
s/這わ/這は/g
s/這い/這ひ/g
s/這う/這ふ/g
s/這え/這へ/g
s/這お/這は/g
s/這ふた/這うた/g
s/這うため/這ふため/g
s/這ふて/這うて/g
s/祝わ/祝は/g
s/祝い/祝ひ/g
s/祝う/祝ふ/g
s/祝え/祝へ/g
s/祝お/祝は/g
s/祝ふた/祝うた/g
s/祝うため/祝ふため/g
s/祝ふて/祝うて/g
s/窺わ/窺は/g
s/窺い/窺ひ/g
s/窺う/窺ふ/g
s/窺え/窺へ/g
s/窺お/窺は/g
s/窺ふた/窺うた/g
s/窺うため/窺ふため/g
s/窺ふて/窺うて/g
s/習わ/習は/g
s/習い/習ひ/g
s/習う/習ふ/g
s/習え/習へ/g
s/習お/習は/g
s/習ふた/習うた/g
s/習うため/習ふため/g
s/習ふて/習うて/g
s/歌わ/歌は/g
s/歌い/歌ひ/g
s/歌う/歌ふ/g
s/歌え/歌へ/g
s/歌お/歌は/g
s/歌ふた/歌うた/g
s/歌うため/歌ふため/g
s/歌ふて/歌うて/g
s/謳わ/謳は/g
s/謳い/謳ひ/g
s/謳う/謳ふ/g
s/謳え/謳へ/g
s/謳お/謳は/g
s/謳ふた/謳うた/g
s/謳うため/謳ふため/g
s/謳ふて/謳うて/g
s/伴わ/伴は/g
s/伴い/伴ひ/g
s/伴う/伴ふ/g
s/伴え/伴へ/g
s/伴お/伴は/g
s/伴ふた/伴うた/g
s/伴うため/伴ふため/g
s/伴ふて/伴うて/g
s/狂わ/狂は/g
s/狂い/狂ひ/g
s/狂う/狂ふ/g
s/狂え/狂へ/g
s/狂お/狂は/g
s/狂ふた/狂うた/g
s/狂うため/狂ふため/g
s/狂ふて/狂うて/g
s/遭わ/遭は/g
s/遭い/遭ひ/g
s/遭う/遭ふ/g
s/遭え/遭へ/g
s/遭お/遭は/g
s/遭ふた/遭うた/g
s/遭うため/遭ふため/g
s/遭ふて/遭うて/g
s/叶わ/叶は/g
s/叶い/叶ひ/g
s/叶う/叶ふ/g
s/叶え/叶へ/g
s/叶お/叶は/g
s/叶ふた/叶うた/g
s/叶うため/叶ふため/g
s/叶ふて/叶うて/g
s/行なわ/行なは/g
s/行ない/行なひ/g
s/行なう/行なふ/g
s/行なえ/行なへ/g
s/行なお/行なは/g
s/行なふた/行なうた/g
s/行なうため/行なふため/g
s/行なふて/行なうて/g
s/戰わ/戰は/g
s/戰い/戰ひ/g
s/戰う/戰ふ/g
s/戰え/戰へ/g
s/戰お/戰は/g
s/戰ふた/戰うた/g
s/戰うため/戰ふため/g
s/戰ふて/戰うて/g
s/奪わ/奪は/g
s/奪い/奪ひ/g
s/奪う/奪ふ/g
s/奪え/奪へ/g
s/奪お/奪は/g
s/奪ふた/奪うた/g
s/奪うため/奪ふため/g
s/奪ふて/奪うて/g
s/呪わ/呪は/g
s/呪い/呪ひ/g
s/呪う/呪ふ/g
s/呪え/呪へ/g
s/呪お/呪は/g
s/呪ふた/呪うた/g
s/呪うため/呪ふため/g
s/呪ふて/呪うて/g

# ## 追加
s/捉え/捉へ/g
s/例え/例へ/g
s/抱え/抱へ/g
s/喩え/喩へ/g
s/數え/數へ/g
s/訴え/訴へ/g
s/迎え/迎へ/g
s/交え/交へ/g
s/考え/考へ/g
s/敎え/敎へ/g
s/与え/與へ/g
s/答え/答へ/g
s/傳え/傳へ/g
s/傳う/傳ふ/g
s/備え/備へ/g
s/閉じ/閉ぢ/g
s/率い/率ゐ/g
s/用い/用ゐ/g
s/抑え/抑へ/g
s/先ず/先づ/g
s/血すじ/血すぢ/g
s/與え/與へ/g
s/表わ/表は/g
s/交わ/交は/g
s/關わ/關は/g
s/終わ/終は/g
s/終え/終へ/g
s/加わ/加は/g
s/加え/加へ/g
s/代わ/代は/g
s/代え/代へ/g
s/變わ/變は/g
s/變え/變へ/g
s/傳わ/傳は/g
s/傳え/傳へ/g
s/替え/替へ/g
s/支え/支へ/g
s/換わ/換は/g
s/換え/換へ/g
s/唱え/唱へ/g
s/憂い/憂ひ/g
s/互い/互ひ/g
s/勢い/勢ひ/g
s/憂う/憂ふ/g
s/危う/危ふ/g
s/憂え/憂へ/g
s/捕らえ/捕らへ/g
s/捕え/捕へ/g
s/攜え/攜へ/g
s/稱え/稱へ/g
s/讚え/讚へ/g
s/控え/控へ/g
s/仕え/仕へ/g
s/應え/應へ/g
s/匂い/匂ひ/g

s/少しずつ/少しづつ/g
s/おおむね/おほむね/g
s/かじ取/かぢ取/g
s/たとえ/たとへ/g
s/いわゆる/いはゆる/g
s/じゃない/ぢやない/g
s/じゃね/ぢやね/g
s/ゆえに/ゆゑに/g
s/ように/やうに/g
s/ような/やうな/g
s/だろう/だらう/g
s/しょうがない/しやうがない/g
s/しょうもない/しやうもない/g
s/しょう。/せう。/g
s/しょう/【しょ|せ】う/g
s/ついに/つひに/g
s/つひで/ついで/g
s/なお、/なほ、/g
s/いる。/ゐる。/g
s/いる/【い|ゐ】る/g
s/いた/【い|ゐ】た/g
s/いて/【い|ゐ】て/g
s/いない/ゐない/g
s/いない/ゐない/g
s/いなかった/ゐなかつた/g
s/いました/ゐました/g
s/いません/ゐません/g
s/います。/ゐます。/g
s/います/【い|ゐ】ます/g
s/くらい/くら【い|ゐ】/g
s/しまう。/しまふ。/g
s/ようだ/やうだ/g
s/そうだ/さうだ/g
s/あろう/あらう/g

s/うえ/う【え|へ】/g
s/さえ/さ【え|へ】/g
s/まえ/ま【え|へ】/g
s/こうして/かうして/g
s/こう/【こ|か】う/g
s/しまう/しま【う|ふ】/g
s/しまい/しま【い|ひ】/g
s/そうな/さうな/g
s/そうに/さうに/g
s/そう/【そ|さ】う/g
s/ほう/【ほ|は】う/g
s/ようやく/やうやく/g
s/よう/【よ|や】う/g
s/ろう/【ろ|ら】う/g
s/出ず/出【ず|づ】/g
s/もらう/もら【う|ふ】/g
s/ちゃう/ちやふ/g

y/ぁぃぅぇぉっゃゅょ/あいうえおつやゆよ/

# ## 御好み
s/エホバ/ヱホバ/g
s/スイッチ/スヰッチ/g
s/ウイスキー/ウヰスキー/g
s/ウイルス/ウヰルス/g
s/ウィルス/ウヰルス/g
s/ウインドウ/ウヰンドウ/g
s/ウィンドウ/ウヰンドウ/g
s/ウェブ/ウヱブ/g
s/ソフトウェア/ソフトウヱア/g
s/ハードウェア/ハードウヱア/g

# 機械變換の補正用
s/缺伸/欠伸/g   # あくび
s/藝草/芸草/g   # うんさう
s/缺缺/欠缺/g   # けんけつ
s/ござゐま/ございま/g   # ござりますのイ音便
s/御座ゐま/御座いま/g
s/しま【え\|へ】/しまへ/g
s/すゐません/すいません/g
s/【い\|ゐ】ただけ/いただけ/g
s/お【い\|ゐ】て/おいて/g
s/つ【い\|ゐ】た/ついた/g
s/つ【い\|ゐ】て/ついて/g
s/づ【い\|ゐ】た/づいた/g
s/つ【い\|ゐ】て/ついて/g
s/書【い\|ゐ】/書い/g
s/願ひ【い\|ひ】た/願ひいた/g
s/描【い\|ゐ】/描い/g
s/聞【い\|ゐ】/聞い/g
s/燒【い\|ゐ】/燒い/g
s/付【い\|ゐ】/付い/g
s/附【い\|ゐ】/附い/g
s/續【い\|ゐ】/續い/g
s/置【い\|ゐ】/置い/g
s/ゐな【い\|ゐ】/ゐない/g
s/叩【い\|ゐ】/叩い/g
s/卷【い\|ゐ】/卷い/g
s/導【い\|ゐ】/導い/g
s/抱【い\|ゐ】/抱い/g
s/強【い\|ゐ】/強い/g
s/開【い\|ゐ】/開い/g
s/着【い\|ゐ】/着い/g
s/著【い\|ゐ】/著い/g
s/招【い\|ゐ】/招い/g
s/引【い\|ゐ】/引い/g
s/拔【い\|ゐ】/拔い/g
s/剥【い\|ゐ】/剥い/g
s/動【い\|ゐ】/動い/g
s/破【い\|ゐ】/破い/g
s/働【い\|ゐ】/働い/g
s/づ【い\|ゐ】/づい/g
s/屆【い\|ゐ】/屆い/g
s/敷【い\|ゐ】/敷い/g
s/驚【い\|ゐ】/驚い/g
s/暴【い\|ゐ】/暴い/g
s/謎め【い\|ゐ】/謎めい/g
s/恥じ/恥ぢ/g
s/かわい【い\|ひ】/かわいい/g
s/【よ\|や】うこそ/ようこそ/g

## 右則が正しい表現。

s/爬蟲類/爬虫類/g   # 蟲はムシ、虫はマムシ
s/天臺宗/天台宗/g
s/臺覽/台覽/g
s/五誡/五戒/g       # 佛教は五戒、耶蘇教は十誡
s/受附/受付/g
s/付録/附録/g
s/付加/附加/g
s/付屬/附屬/g

## 右則が正しい表現。
s/老ひ/老い/g
s/覺へ/覺え/g
s/悔ひ/悔い/g
s/超へ/超え/g
s/增へ/增え/g
s/見へ/見え/g
s/絶へ/絶え/g
s/燃へ/燃え/g
s/冷へ/冷え/g
s/肥へ/肥え/g
s/費へ/費え/g
s/聞こへ/聞こえ/g
s/植へ/植ゑ/g
s/植え/植ゑ/g
s/飢へ/飢ゑ/g
s/飢え/飢ゑ/g
s/据へ/据ゑ/g
s/据え/据ゑ/g

s/ちやゐます/ちやひます/g
s/ありがとう/ありがたう/g
s/いずく/いづく/g
s/いずこ/いづこ/g
s/いずみ/いづみ/g
s/いずれ/いづれ/g
s/おとこ/をとこ/g
s/おんな/をんな/g
s/おかしい/をかしい/g
s/おのずから/おのづから/g
s/かほり/かをり/g
s/しずか/しづか/g
s/すじ/すぢ/g
s/たうたう/とうとう/g       # とと（止止）が延音したもの。
s/まず、/まづ、/g
s/まずは/まづは/g
s/みずから/みづから/g
s/みずほ/みづほ/g
s/めずらし/めづらし/g
s/をきな/おきな/g
s/をみな/おみな/g
