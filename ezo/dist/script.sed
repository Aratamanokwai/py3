# -*- coding: utf-8 -*-
#
# # 較正の手引

# ## 使用方法
# ```sh
# $ sed -f correct.sed text.txt
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
# ### 一覽
# s/新字/正字/g
# 但し、
# 必ずしも左側の新字表現を右側の正字表現に直せば可いといふものではない。
#
s/亜鈴/啞鈴/g
s/暗唱/暗誦/g
s/暗夜/闇夜/g
s/優俊/優駿/g
s/意向/意嚮/g
s/衣装/衣裳/g
s/委縮/萎縮/g
s/一獲千金/一攫千金/g
s/陰影/陰翳/g
s/隠滅/湮滅/g
s/英才/穎才/g
s/英知/叡智/g
s/憶病/臆病/g
s/恩義/恩誼/g
s/耕運機/耕耘機/g
s/交歓/交驩/g
s/交差/交叉/g
s/高進/亢進/g
s/更正/甦生/g
s/香典/香奠/g
s/高騰/昂騰/g
s/興奮/亢奮/g
s/高揚/昂揚/g
s/効率/效率/g
s/講和/媾和/g
s/火炎/火焰/g
s/画期的/劃期的/g
s/格闘/挌闘/g
s/格好/恰好/g
s/活発/活潑/g
s/格幅/恰幅/g
s/個条書/箇條書/g
s/干害/旱害/g
s/間欠/間歇/g
s/肝心/肝腎/g
s/関数/函數/g
s/干天/旱天/g
s/乾留/乾溜/g
s/強欲/強慾/g
s/合弁/合辦/g
s/旧跡/舊蹟/g
s/糾明/糺明/g
s/気炎/気焔/g
s/飢餓/饑餓/g
s/喜々/嬉々/g
s/企画/企劃/g
s/奇形/畸形/g
s/希元素/稀元素/g
s/希釈/稀釋/g
s/奇人/畸人/g
s/希少/稀少/g
s/棄損/毀損/g
s/希代/稀代/g
s/機知/機智/g
s/喫水/吃水/g
s/気迫/氣魄/g
s/希薄/稀薄/g
s/奇弁/詭辯/g
s/危弁/詭辯/g
s/供宴/饗宴/g
s/強固/鞏固/g
s/橋頭保/橋頭堡/g
s/供応/饗應/g
s/喜遊曲/嬉遊曲/g
s/凶行/兇行/g
s/凶漢/兇漢/g
s/凶器/兇器/g
s/凶刃/兇刃/g
s/凶暴/兇暴/g
s/凶変/兇變/g
s/共役/共軛/g
s/拠金/醵金/g
s/拠出/醵出/g
s/希硫酸/稀硫酸/g
s/禁固/禁錮/g
s/均整/均齊/g
s/義援/義捐/g
s/御者/馭者/g
s/魚労/魚撈/g
s/技量/伎倆/g
s/吟唱/吟誦/g
s/区画/區劃/g
s/掘削/掘鑿/g
s/快活/快闊/g
s/回転/廻轉/g
s/回覧/廻覽/g
s/回復/恢復/g
s/花弁/花瓣/g
s/回廊/囘游/g
s/鉱業/礦業/g
s/広壮/宏壯/g
s/鉱石/礦石/g
s/広大/宏大/g
s/広範/廣汎/g
s/広野/曠野/g
s/画期的/劃期的/g
s/画然/劃然/g
s/拡大/廓大/g     # 擴大でも可
s/管弦/管絃/g
s/歓待/款待/g     # 歡待も可
s/貫録/貫禄/g
s/訓戒/訓誡/g
s/薫蒸/燻蒸/g
s/薫製/燻製/g
s/計画/計劃/g
s/傾向/傾嚮/g
s/敬謙/敬虔/g
s/係争/繋爭/g
s/係船/繋船/g
s/係属/繋屬/g
s/係留/繋留/g
s/決壊/決潰/g
s/恐喝/脅喝/g
s/決起/蹶起/g
s/決別/訣別/g
s/肩甲骨/肩胛骨/g
s/険阻/嶮岨/g
s/建坪率/建蔽率/g
s/研摩/研磨/g
s/激高/激昂/g
s/下克上/下尅上/g
s/月食/月蝕/g
s/弦歌/絃歌/g
s/元凶/元兇/g
s/厳然/儼然/g
s/幻惑/眩惑/g
s/拘引/勾引/g
s/控除/扣除/g
s/広報/弘報/g
s/枯渇/涸渴/g
s/古希/古稀/g
s/骨格/骨骼/g
s/雇用/雇傭/g
s/混交/混淆/g
s/混然/渾然/g
s/根底/根柢/g
s/倉皇/蒼惶/g
s/相克/相剋/g
s/装丁/裝釘/g
# さうめつ	剿滅	みなごろし
# さうめつ	掃滅	はらひのけほろぼすこと
s/削岩/鑿岩/g
s/酢酸/醋酸/g
s/賛仰/讚仰/g
s/三弦/三絃/g
s/三差/三叉/g
s/賛辞/讚辞/g
s/散水/撒水/g
s/賛美/讚美/g
s/散布/撒布/g
s/障害/障礙/g
s/象眼/象嵌/g
s/座視/坐視/g
s/座州/坐洲/g
s/座礁/坐礁/g
s/雑踏/雜沓/g
s/集荷/蒐荷/g
s/色欲/色慾/g
s/刺激/刺戟/g
s/死体/屍體/g
s/質草/質種/g
s/七転八倒/七顚八倒/g
s/十戒/十誡/g
s/紫班/紫斑/g
s/死沒/死歿/g
s/車両/車輌/g
s/終息/終熄/g
s/集落/聚落/g
s/俊才/駿才/g
s/俊足/駿足/g
s/俊馬/駿馬/g
s/称賛/稱讚/g
s/賞賛/賞讚/g
s/昇叙/陞敍/g
s/食事療法/食餌療法/g
s/食尽/蝕甚/g
s/食欲/食慾/g
s/試練/試煉/g
s/侵食/侵蝕/g
s/浸食/浸蝕/g
s/針術/鍼術/g
s/真跡/眞蹟/g
s/伸長/伸暢/g
s/浸透/滲透/g
s/心拍/心搏/g
s/侵略/侵掠/g
s/順化/馴化/g
s/順守/遵守/g
s/純朴/醇朴/g
s/蒸留/蒸溜/g
s/叙情/抒情/g
s/尋問/訊問/g
s/衰退/衰頽/g
s/消夏/銷夏/g
s/消却/銷卻/g
s/焦燥/焦躁/g
s/消沈/銷沈/g
s/勝利/捷利/g     # 勝利（しようり）のままでも可
s/先鋭/尖鋭/g
s/選考/銓衡/g
s/船倉/船艙/g
s/扇情/煽情/g
s/戦々恐々/戰々兢々/g
s/専断/擅斷/g
s/扇動/煽動/g
s/先兵/尖兵/g
s/戦沒/戰歿/g
s/冗舌/饒舌/g
s/絶賛/絶讃/g
s/総合/綜合/g
s/総菜/惣菜/g
s/阻喪/沮喪/g
s/阻止/沮止/g
s/疎水/疏水/g
s/疎通/疏通/g
s/疎明/疏明/g
s/族生/簇生/g
s/退色/褪色/g
s/退勢/頽勢/g
s/台頭/擡頭/g
s/退廃/頽廢/g
s/台風/颱風/g
s/大欲/大慾/g
s/倒壊/倒潰/g
s/高根の花/高嶺の花/g
s/踏襲/蹈襲/g
s/炭鉱/炭礦/g
s/嘆願/歎願/g
s/端座/端坐/g
s/短編/短篇/g
s/奪略/奪掠/g
# だんこ	断乎>>断固
s/暖房/煖房/g
s/暖炉/煖爐/g
s/抽選/抽籤/g
s/知能/智能/g
s/知謀/智謀/g
s/長編/長篇/g
s/注解/註解/g
s/注釈/註釋/g
s/注文/註文/g
s/沈殿/沈澱/g
s/抵触/牴觸/g
s/丁重/鄭重/g
s/丁寧/叮嚀/g
s/停泊/碇泊/g
s/鳥観/鳥瞰/g
s/鳥観図/鳥瞰圖/g
s/転倒/顚倒//g
s/展転/輾轉/g
s/転覆/顚覆/g
s/条虫/絛蟲/g
s/殿部/臀部/g
s/殿粉/澱粉/g
s/特集/特輯/g
s/途絶/杜絶/g
s/廃虚/廢墟/g
s/背徳/悖徳/g
s/配列/排列/g
s/放棄/抛棄/g
s/芳純/芳醇/g
s/包帯/繃帶/g
s/包丁/庖丁/g
s/放物線/抛物線/g
s/白亜/白堊/g
s/薄幸/薄倖/g
s/拍動/搏動/g
s/破砕/破摧/g
s/発酵/醗酵/g
s/波乱/波瀾/g
s/反旗/叛旗/g
s/反逆/叛逆/g
s/繁殖/蕃殖/g
s/班点/斑點/g
s/反発/反撥/g
s/反乱/叛亂/g
s/梅雨/黴雨/g
s/梅毒/黴毒/g
s/買弁/買辦/g
s/防圧/防遏/g
s/妨害/妨礙/g
s/防御/防禦/g
# ばうだい	厖大	形容動詞で、量や規模が大きいさま。
# ばうだい	膨大	サ変動詞で、膨れて大きくなること。
s/膨張/膨脹/g
s/暴露/曝露/g
s/抜粋/拔萃/g
s/蛮族/蕃族/g
s/飛語/蜚語/g
s/非才/菲才/g
s/披歴/披瀝/g
s/広野/曠野/g
s/病沒/病歿/g
s/風光明美/風光明媚/g
s/風刺/諷刺/g
s/風諭/諷喩/g
s/敷延/布衍/g
s/腐食/腐蝕/g
s/普段/不斷/g
s/符丁/符牒/g
s/腐乱/腐爛/g
s/粉装/扮裝/g
s/格好/恰好/g
s/物欲/物慾/g
s/分留/分溜/g
s/漂然/飄然/g
s/辺境/邊疆/g
s/編集/編輯/g
s/片頭痛/偏頭痛/g
s/弁護/辯護/g
s/弁当/辨當/g
s/偏平/扁平/g
s/弁髪/辮髮/g
s/保育/哺育/g
s/崩壊/崩潰/g
s/奉持/捧持/g
s/補佐/輔佐/g
s/舗装/鋪裝/g
s/補導/輔導/g
s/保母/保姆/g
s/保塁/堡塁/g
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
s/無欲/無慾/g
s/名誉棄損/名譽毀損/g
s/名誉欲/名譽慾/g
s/名誉/名譽/g
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
s/乱掘/濫掘/g
s/乱作/濫作/g
s/乱造/濫造/g
s/乱読/濫読/g
s/乱発/濫発/g
s/乱費/濫費/g
s/乱用/濫用/g
s/留飲/溜飮/g
s/留出/溜出/g
s/里謡/俚謠/g
# りかい	理解	内容、意味などが分かること。
# りくわい	理會	物事の道理を會得すること。
s/理屈/理窟/g
s/利口/悧口/g
s/理知/理智/g
s/離反/離叛/g
s/略奪/掠奪/g
s/輪郭/輪廓/g
s/了見/了簡/g
s/連係/連繋/g
s/練炭/煉炭/g
s/練乳/煉乳/g
s/練摩/錬磨/g # れんま	練（錬）磨>>練摩（新）
# わけ	訣	訳（譯）は宛字で本來「わけ」の訓は無い
s/慰謝料/慰藉料/g
s/回向/廻向/g
s/温暖/溫煖/g
# ## 追加
s/栄養/營養/g
s/ホ乳/哺乳/g
s/障害者/障礙者/g

# ## 新字の單純舊字化（なんちゃって正字）に對應
s/亞鈴/啞鈴/g
s/衣裝/衣裳/g
s/隱滅/湮滅/g
s/交歡/交驩/g
s/畫期的/劃期的/g
s/格鬪/挌鬪/g
s/活發/活潑/g
s/個條書/箇條書/g
s/間缺/間歇/g
s/關數/函數/g
s/舊跡/舊蹟/g
s/氣炎/氣焔/g
s/企畫/企劃/g
s/希釋/稀釋/g
s/氣迫/氣魄/g
s/供應/饗應/g
s/據金/醵金/g
s/據出/醵出/g
s/魚勞/魚撈/g
s/區畫/區劃/g
s/回轉/廻轉/g
s/回覽/廻覽/g
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
s/計畫/計劃/g
s/係爭/繋爭/g
s/係屬/繋屬/g
s/決壞/決潰/g
s/險阻/嶮岨/g
s/嚴然/儼然/g
s/廣報/弘報/g
s/裝丁/裝釘/g
s/贊仰/讚仰/g
s/贊辭/讚辭/g
s/贊美/讚美/g
s/雜踏/雜沓/g
s/死體/屍體/g
s/車兩/車輌/g
s/食盡/蝕甚/g
s/眞跡/眞蹟/g
s/消卻/銷卻/g
s/戰々恐々/戰々兢々/g
s/專斷/擅斷/g
s/戰沒/戰歿/g
s/絶贊/絶讚/g
s/總合/綜合/g
s/總菜/惣菜/g
s/臺頭/擡頭/g
s/退廢/頽廢/g
s/臺風/颱風/g
s/炭鑛/炭礦/g
s/暖爐/煖爐/g
s/注釋/註釋/g
s/抵觸/牴觸/g
s/鳥觀/鳥瞰/g
s/鳥觀圖/鳥瞰圖/g
s/轉倒/顚倒//g
s/展轉/輾轉/g
s/轉覆/顚覆/g
s/條蟲/絛蟲/g
s/廢虚/廢墟/g
s/妨碍/妨礙/g
s/白亞/白堊/g
s/發酵/醗酵/g
s/波亂/波瀾/g
s/班點/斑點/g
s/反發/反撥/g
s/反亂/叛亂/g
s/防壓/防遏/g
s/拔粹/拔萃/g
s/蠻族/蕃族/g
s/廣野/曠野/g
s/腐亂/腐爛/g
s/粉裝/扮裝/g
s/邊境/邊疆/g
s/舖裝/鋪裝/g
s/名譽棄損/名譽毀損/g
s/名譽欲/名譽慾/g
s/亂掘/濫掘/g
s/亂作/濫作/g
s/亂造/濫造/g
s/亂讀/濫讀/g
s/亂發/濫發/g
s/亂費/濫費/g
s/亂用/濫用/g
s/里謠/俚謠/g
# ## 追加
s/榮養/營養/g
s/障碍者/障礙者/g

# ## 差別用語対策
# s/中国/支那/g
# s/親中/親支/g

# ## 正假名遣への變換
s/てしまう/てしまふ/g
s/てしまい/てしまひ/g
s/ている/てゐる/g
s/ていない/てゐない/g
s/ていた/てゐた/g
s/そういう/さういふ/g
s/やろう/やらう/g
s/できるよう/できるやう/g

# ## ハ行四段
s/笑わ/笑は/g
s/笑い/笑ひ/g
s/笑う。/笑ふ。/g
s/笑うと/笑ふと/g
s/笑うに/笑ふに/g
s/笑うべ/笑ふべ/g
s/笑うこと/笑ふこと/g
s/笑え/笑へ/g
s/笑お/笑は/g
s/笑う/[笑う|笑ふ]/g
s/笑ふた/笑うた/g
s/笑ふて/笑うて/g
s/救わ/救は/g
s/救い/救ひ/g
s/救う。/救ふ。/g
s/救うと/救ふと/g
s/救うに/救ふに/g
s/救うべ/救ふべ/g
s/救うこと/救ふこと/g
s/救え/救へ/g
s/救お/救は/g
s/救う/[救う|救ふ]/g
s/救ふた/救うた/g
s/救ふて/救うて/g
s/失わ/失は/g
s/失い/失ひ/g
s/失う。/失ふ。/g
s/失うと/失ふと/g
s/失うに/失ふに/g
s/失うべ/失ふべ/g
s/失うこと/失ふこと/g
s/失え/失へ/g
s/失お/失は/g
s/失う/[失う|失ふ]/g
s/失ふた/失うた/g
s/失ふて/失うて/g
s/障碍わ/障碍は/g
s/障碍い/障碍ひ/g
s/障碍う。/障碍ふ。/g
s/障碍うと/障碍ふと/g
s/障碍うに/障碍ふに/g
s/障碍うべ/障碍ふべ/g
s/障碍うこと/障碍ふこと/g
s/障碍え/障碍へ/g
s/障碍お/障碍は/g
s/障碍う/[障碍う|障碍ふ]/g
s/障碍ふた/障碍うた/g
s/障碍ふて/障碍うて/g
s/扱わ/扱は/g
s/扱い/扱ひ/g
s/扱う。/扱ふ。/g
s/扱うと/扱ふと/g
s/扱うに/扱ふに/g
s/扱うべ/扱ふべ/g
s/扱うこと/扱ふこと/g
s/扱え/扱へ/g
s/扱お/扱は/g
s/扱う/[扱う|扱ふ]/g
s/扱ふた/扱うた/g
s/扱ふて/扱うて/g
s/慕わ/慕は/g
s/慕い/慕ひ/g
s/慕う。/慕ふ。/g
s/慕うと/慕ふと/g
s/慕うに/慕ふに/g
s/慕うべ/慕ふべ/g
s/慕うこと/慕ふこと/g
s/慕え/慕へ/g
s/慕お/慕は/g
s/慕う/[慕う|慕ふ]/g
s/慕ふた/慕うた/g
s/慕ふて/慕うて/g
s/買わ/買は/g
s/買い/買ひ/g
s/買う。/買ふ。/g
s/買うと/買ふと/g
s/買うに/買ふに/g
s/買うべ/買ふべ/g
s/買うこと/買ふこと/g
s/買え/買へ/g
s/買お/買は/g
s/買う/[買う|買ふ]/g
s/買ふた/買うた/g
s/買ふて/買うて/g
s/飼わ/飼は/g
s/飼い/飼ひ/g
s/飼う。/飼ふ。/g
s/飼うと/飼ふと/g
s/飼うに/飼ふに/g
s/飼うべ/飼ふべ/g
s/飼うこと/飼ふこと/g
s/飼え/飼へ/g
s/飼お/飼は/g
s/飼う/[飼う|飼ふ]/g
s/飼ふた/飼うた/g
s/飼ふて/飼うて/g
s/拂わ/拂は/g
s/拂い/拂ひ/g
s/拂う。/拂ふ。/g
s/拂うと/拂ふと/g
s/拂うに/拂ふに/g
s/拂うべ/拂ふべ/g
s/拂うこと/拂ふこと/g
s/拂え/拂へ/g
s/拂お/拂は/g
s/拂う/[拂う|拂ふ]/g
s/拂ふた/拂うた/g
s/拂ふて/拂うて/g
s/問わ/問は/g
s/問い/問ひ/g
s/問う。/問ふ。/g
s/問うと/問ふと/g
s/問うに/問ふに/g
s/問うべ/問ふべ/g
s/問うこと/問ふこと/g
s/問え/問へ/g
s/問お/問は/g
s/問う/[問う|問ふ]/g
s/問ふた/問うた/g
s/問ふて/問うて/g
s/願わ/願は/g
s/願い/願ひ/g
s/願う。/願ふ。/g
s/願うと/願ふと/g
s/願うに/願ふに/g
s/願うべ/願ふべ/g
s/願うこと/願ふこと/g
s/願え/願へ/g
s/願お/願は/g
s/願う/[願う|願ふ]/g
s/願ふた/願うた/g
s/願ふて/願うて/g
s/謂わ/謂は/g
s/謂い/謂ひ/g
s/謂う。/謂ふ。/g
s/謂うと/謂ふと/g
s/謂うに/謂ふに/g
s/謂うべ/謂ふべ/g
s/謂うこと/謂ふこと/g
s/謂え/謂へ/g
s/謂お/謂は/g
s/謂う/[謂う|謂ふ]/g
s/謂ふた/謂うた/g
s/謂ふて/謂うて/g
s/云わ/云は/g
s/云い/云ひ/g
s/云う。/云ふ。/g
s/云うと/云ふと/g
s/云うに/云ふに/g
s/云うべ/云ふべ/g
s/云うこと/云ふこと/g
s/云え/云へ/g
s/云お/云は/g
s/云う/[云う|云ふ]/g
s/云ふた/云うた/g
s/云ふて/云うて/g
s/言わ/言は/g
s/言い/言ひ/g
s/言う。/言ふ。/g
s/言うと/言ふと/g
s/言うに/言ふに/g
s/言うべ/言ふべ/g
s/言うこと/言ふこと/g
s/言え/言へ/g
s/言お/言は/g
s/言う/[言う|言ふ]/g
s/言ふた/言うた/g
s/言ふて/言うて/g
s/いわ/いは/g
s/いい/[いい|いひ]/g
s/いう。/いふ。/g
s/いうと/いふと/g
s/いうに/いふに/g
s/いうべ/いふべ/g
s/いうこと/いふこと/g
s/いえ/いへ/g
s/いお/いは/g
s/いう/[いう|いふ]/g
s/いふた/いうた/g
s/いふて/いうて/g
s/味わわ/味はは/g
s/味わい/味はひ/g
s/味わう。/味はふ。/g
s/味わうと/味はふと/g
s/味わうに/味はふに/g
s/味わうべ/味はふべ/g
s/味わうこと/味はふこと/g
s/味わえ/味はへ/g
s/味わお/味はは/g
s/味わう/[味はう|味はふ]/g
s/味わふた/味はうた/g
s/味わふて/味はうて/g
s/誘わ/誘は/g
s/誘い/誘ひ/g
s/誘う。/誘ふ。/g
s/誘うと/誘ふと/g
s/誘うに/誘ふに/g
s/誘うべ/誘ふべ/g
s/誘うこと/誘ふこと/g
s/誘え/誘へ/g
s/誘お/誘は/g
s/誘う/[誘う|誘ふ]/g
s/誘ふた/誘うた/g
s/誘ふて/誘うて/g
s/惑わ/惑は/g
s/惑い/惑ひ/g
s/惑う。/惑ふ。/g
s/惑うと/惑ふと/g
s/惑うに/惑ふに/g
s/惑うべ/惑ふべ/g
s/惑うこと/惑ふこと/g
s/惑え/惑へ/g
s/惑お/惑は/g
s/惑う/[惑う|惑ふ]/g
s/惑ふた/惑うた/g
s/惑ふて/惑うて/g
s/通わ/通は/g
s/通い/通ひ/g
s/通う。/通ふ。/g
s/通うと/通ふと/g
s/通うに/通ふに/g
s/通うべ/通ふべ/g
s/通うこと/通ふこと/g
s/通え/通へ/g
s/通お/通は/g
s/通う/[通う|通ふ]/g
s/通ふた/通うた/g
s/通ふて/通うて/g
s/疑わ/疑は/g
s/疑い/疑ひ/g
s/疑う。/疑ふ。/g
s/疑うと/疑ふと/g
s/疑うに/疑ふに/g
s/疑うべ/疑ふべ/g
s/疑うこと/疑ふこと/g
s/疑え/疑へ/g
s/疑お/疑は/g
s/疑う/[疑う|疑ふ]/g
s/疑ふた/疑うた/g
s/疑ふて/疑うて/g
s/違わ/違は/g
s/違い/違ひ/g
s/違う。/違ふ。/g
s/違うと/違ふと/g
s/違うに/違ふに/g
s/違うべ/違ふべ/g
s/違うこと/違ふこと/g
s/違え/違へ/g
s/違お/違は/g
s/違う/[違う|違ふ]/g
s/違ふた/違うた/g
s/違ふて/違うて/g
s/行わ/行は/g
s/行い/行ひ/g
s/行う。/行ふ。/g
s/行うと/行ふと/g
s/行うに/行ふに/g
s/行うべ/行ふべ/g
s/行うこと/行ふこと/g
s/行え/行へ/g
s/行お/行は/g
s/行う/[行う|行ふ]/g
s/行ふた/行うた/g
s/行ふて/行うて/g
s/襲わ/襲は/g
s/襲い/襲ひ/g
s/襲う。/襲ふ。/g
s/襲うと/襲ふと/g
s/襲うに/襲ふに/g
s/襲うべ/襲ふべ/g
s/襲うこと/襲ふこと/g
s/襲え/襲へ/g
s/襲お/襲は/g
s/襲う/[襲う|襲ふ]/g
s/襲ふた/襲うた/g
s/襲ふて/襲うて/g
s/構わ/構は/g
s/構い/構ひ/g
s/構う。/構ふ。/g
s/構うと/構ふと/g
s/構うに/構ふに/g
s/構うべ/構ふべ/g
s/構うこと/構ふこと/g
s/構え/構へ/g
s/構お/構は/g
s/構う/[構う|構ふ]/g
s/構ふた/構うた/g
s/構ふて/構うて/g
s/負わ/負は/g
s/負い/負ひ/g
s/負う。/負ふ。/g
s/負うと/負ふと/g
s/負うに/負ふに/g
s/負うべ/負ふべ/g
s/負うこと/負ふこと/g
s/負え/負へ/g
s/負お/負は/g
s/負う/[負う|負ふ]/g
s/負ふた/負うた/g
s/負ふて/負うて/g
s/會わ/會は/g
s/會い/會ひ/g
s/會う。/會ふ。/g
s/會うと/會ふと/g
s/會うに/會ふに/g
s/會うべ/會ふべ/g
s/會うこと/會ふこと/g
s/會え/會へ/g
s/會お/會は/g
s/會う/[會う|會ふ]/g
s/會ふた/會うた/g
s/會ふて/會うて/g
s/合わ/合は/g
s/合い/合ひ/g
s/合う。/合ふ。/g
s/合うと/合ふと/g
s/合うに/合ふに/g
s/合うべ/合ふべ/g
s/合うこと/合ふこと/g
s/合え/合へ/g
s/合お/合は/g
s/合う/[合う|合ふ]/g
s/合ふた/合うた/g
s/合ふて/合うて/g
s/使わ/使は/g
s/使い/使ひ/g
s/使う。/使ふ。/g
s/使うと/使ふと/g
s/使うに/使ふに/g
s/使うべ/使ふべ/g
s/使うこと/使ふこと/g
s/使え/使へ/g
s/使お/使は/g
s/使う/[使う|使ふ]/g
s/使ふた/使うた/g
s/使ふて/使うて/g
s/想わ/想は/g
s/想い/想ひ/g
s/想う。/想ふ。/g
s/想うと/想ふと/g
s/想うに/想ふに/g
s/想うべ/想ふべ/g
s/想うこと/想ふこと/g
s/想え/想へ/g
s/想お/想は/g
s/想う/[想う|想ふ]/g
s/想ふた/想うた/g
s/想ふて/想うて/g
s/思わ/思は/g
s/思い/思ひ/g
s/思う。/思ふ。/g
s/思うと/思ふと/g
s/思うに/思ふに/g
s/思うべ/思ふべ/g
s/思うこと/思ふこと/g
s/思え/思へ/g
s/思お/思は/g
s/思う/[思う|思ふ]/g
s/思ふた/思うた/g
s/思ふて/思うて/g
s/念わ/念は/g
s/念い/念ひ/g
s/念う。/念ふ。/g
s/念うと/念ふと/g
s/念うに/念ふに/g
s/念うべ/念ふべ/g
s/念うこと/念ふこと/g
s/念え/念へ/g
s/念お/念は/g
s/念う/[念う|念ふ]/g
s/念ふた/念うた/g
s/念ふて/念うて/g

#  機種依存文字。
s/勝どき/勝鬨/g

# ## 追加
s/訴え/訴へ/g
s/迎え/迎へ/g
s/交え/交へ/g
s/考え/考へ/g
s/教え/教へ/g
s/与え/與へ/g
s/答え/答へ/g
s/伝え/傳へ/g
s/備え/備へ/g
s/閉じ/閉ぢ/g
s/率い/率ゐ/g
s/用い/用ゐ/g
s/抑え/抑へ/g

s/関わ/關は/g
s/終わ/終は/g
s/終へ/終へ/g
s/加わ/加は/g
s/加へ/加へ/g
s/代わ/代は/g
s/代へ/代へ/g
s/変わ/變は/g
s/変え/變へ/g
s/伝わ/傳は/g
s/伝え/傳へ/g
s/替え/替へ/g
s/換え/換へ/g
s/唱え/唱へ/g
s/憂い/憂ひ/g
s/憂う/憂ふ/g
s/憂え/憂へ/g

s/匂い/匂ひ/g
s/おおむね/おほむね/g
s/おおい/おほい/g
s/かじ取/かぢ取/g
s/たとえ/たとへ/g
s/いわゆる/いはゆる/g
s/じゃない/ぢやない/g
s/しょう/せう/g
s/ように/やうに/g
s/ような/やうな/g
s/だろう/だらう/g
s/しょう。/せう。/g
s/ついに/つひに/g
s/なお、/なほ、/g
s/いる。/ゐる。/g
s/いた。/ゐた。/g
s/いない。/ゐない。/g
s/いなかった/ゐなかつた/g
s/います。/ゐます。/g
s/しまう。/しまふ。/g
s/ようだ/やうだ/g
s/ようだ/やうだ/g
s/そうだ/さうだ/g
s/あろう/あらう/g

s/いる/[いる|ゐる]/g
s/いない/[いない|ゐない]/g
s/いた/[いた|ゐた]/g
s/いて/[いて|ゐて]/g
s/います/[います|ゐます]/g
s/いました/ゐました/g
s/いません/ゐません/g
s/うえ/[うえ|うへ]/g
s/こう/[こう|かう]/g
s/しまう/[しまう|しまふ]/g
s/しまい/[しまい|しまひ]/g
s/そう/[そう|さう]/g
s/よう/[よう|やう]/g
s/ろう/[ろう|らう]/g
s/お[いて|ゐて]/おいて/g
s/つ[いて|ゐて]/ついて/g

# # 新字/正字の對應
y/亜悪圧囲医為壱飲隠欝営栄衛駅円艶/亞惡壓圍醫爲壹飮隱鬱營榮衞驛圓艷/
y/塩奥応欧殴穏桜仮価画届会壊懐絵拡/鹽奧應歐毆穩櫻假價畫屆會壞懷繪擴/
y/覚学岳楽殻勧巻歓缶観関巌顔陥帰/覺學嶽樂殼勸卷歡罐觀關巖顏陷歸/
y/気亀偽戯犠旧拠挙峡挟狭暁区駆勲径/氣龜僞戲犧舊據擧峽挾狹曉區驅勳徑/
y/恵渓経継茎蛍軽鶏芸欠倹剣圏検権献/惠溪經繼莖螢輕鷄藝缺儉劍圈檢權獻/
y/県険顕験厳効拠広恒鉱号国済砕冊/縣險顯驗嚴效據廣恆鑛號國濟碎册/
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
# 追加(R021130)
y/煙却娘糸携填涛潅熙珱楕桧梼梹檪/烟卻孃絲攜塡濤灌煕瓔橢檜檮檳櫟/
y/亘卆聟枦渊尓畄翆軣鈬鼡禀竃筝緕/亙卒婿櫨淵爾留翠轟鐸鼠稟竈箏纃/
y/伜僣侭弯忰抬撹昿畴皐碍砿砺舮薮/倅僭儘彎悴擡攪曠疇皋礙礦礪艫藪/
y/鈩鑚陏隷覇虱蝿蛎褒諌弐賎迩隣頚/鑪鑽隋隸霸蝨蠅蠣襃諫貳賤邇鄰頸/
y/鰛鯵鴬鷏麸斎尭槙瑶遥/鰮鰺鶯鷆麩齋堯槇瑤遙/

# 機種依存文字。
y/鴎殺横贈/鷗殺橫贈/
#y/鴎殺闘横贈/鷗殺鬭橫贈/

y/ぁぃぅぇぉっゃゅょ/あいうえおつやゆよ/

##  注意點の指摘。
s/制御/制[馭|禦]/g
## 牆壁	かきとかべと
## 障壁	妨げとなるもののこと。「關税―」
s/障壁/[牆壁|障壁]/g
## 情義	人情と義理のこと。
## 情誼	人とつきあふ上での人情や誠意のこと。
s/情義/[情誼|情義]/g
## 收集	寄せ集めること。「ごみの―」
## 蒐集	コレクション。「切手の−」
s/収集/[收集|蒐集]/g
## 壞亂	やぶれ亂れること
## 潰亂	ちりぢりに亂れること
s/壊乱/[壞亂|潰亂]/g
## 確乎	しつかりしてゐるさま（副詞）確乎として、確乎たる存在である。
## 確固	しつかりして固いこと（名詞）
s/確固/[確乎|確固]/g

# ## 御好み
# y/着/著/g   # 著は正字、着は行書體
# y/笑/咲/g   # 咲は笑の古字、漢文では同字
s/スイッチ/スヰッチ/g
s/ウイスキー/ウヰスキー/g
s/ウイルス/ウヰルス/g

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
# 「仕樣書」は「しヤウしよ」
# 「〜のヨオだ」も「樣」だから「ヤウ」
# ※　要するに、「ヨオ」を機械的に「やう」と變換しては駄目！

# 機械變換の補正用
s/缺缺/欠缺/g   # けんけつ
s/缺伸/欠伸/g   # あくび
s/藝草/芸草/g   # うんさう
s/ござ[います|ゐます]/ございます/g
s/御座[います|ゐます]/御座います/g
s/ござゐま/ございま/g
s/御座ゐま/御座いま/g

## 右則が正しい表現。
s/爬蟲類/爬虫類/g
s/天臺宗/天台宗/g
s/臺覽/台覽/g
s/かほり/かをり/g
s/悔ひ/悔い/g
s/老ひ/老い/g
s/超へ/超え/g
s/見へ/見え/g
s/覺へ/覺え/g
s/をきな/おきな/g
s/をみな/おみな/g
s/おとこ/をとこ/g
s/おんな/をんな/g
# ### 蛇足
#  - 自稱の「余」は「餘」ではない。
#  - 自稱の「予」は「豫」ではない。
#  - 「強」は「口」でなくとも可い。「ム」が正字。
#  - 「回」は「囘」でなくとも可い。「回」が正字で「囘」は古字。
