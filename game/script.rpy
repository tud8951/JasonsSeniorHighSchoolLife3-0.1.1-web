# region Character definitions
define j = Character("杰森")
define sf = Character("四风")
define d = Character("丁真")
define jg = Character("教官")
define c = Character("蔡忆梦")
define someone = Character("某人")
define syq = Character("三月七")
define gg = Character("刚哥")
define x = Character("小帕")
define m = Character("马厂")
define cg = Character("葱哥")
define jh = Character("荆华", who_font="STFANGSO.TTF", what_font="STFANGSO.TTF")
define hy = Character("海燕老师")
define sj = Character("树君老师")
define ld = Character("卢丹（年级主任）")
define sz = Character("邵湛")
define ty = Character("天宇")
define yy = Character("干夭")
define jw = Character("十二班纪委")
define yf = Character("扬帆")
define wlls = Character("物理老师")
define hxls = Character("化学老师")
define lsy = Character("李时雨")
define knx = Character("康乃馨")
define zhw = Character("赵宏伟")
define xq = Character("小曲")
define hky = Character("韩子瑶")
define xian = Character("刘昊（大仙）")
define zyy = Character("张依依")
define stt = Character("单桐桐")
define pxy = Character("朴欣怡")
define classmate_a = Character("同学甲")
define classmate_b = Character("同学乙")
define dy = Character("店员")
#endregion

# region Image definitions
image Sun:
    "images/sun.jpg"
    zoom 3
image cloud:
    "images/cloud.jpg"
    zoom 3
image outschool:
    "images/outschool/1.jpg"
    zoom 1.5
image outschool2:
    "images/outschool/2.jpg"
    zoom 1.5
image playground:
    "images/playground/1.jpg"
    zoom 1.5
image playground2:
    "images/playground/2.jpg"
    zoom 3
image classroom:
    "images/classroom/1.jpg"
    zoom 1.5
image classroom2:
    "images/classroom/2.jpg"
    zoom 1.5
image classroom3:
    "images/classroom/3.jpg"
    zoom 1.5
image classroom4:
    "images/classroom/4.jpg"
    zoom 2.4
image blackboard:
    "images/blackboard.jpg"
    zoom 1.5
image classroom5:
    "images/classroom/5.jpg"
    zoom 2.4
image jg:
    "images/jg.png"
    zoom 0.5
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 580
image bus:
    "images/bus.jpg"
    zoom 3
image ercihanshu:
    "images/ercihanshu.jpg"
    zoom 1
image bag:
    "images/bag.png"
    zoom 0.5
image notes:
    "images/notes.png"
    zoom 0.8
image chinesebook:
    "images/chinesebook.png"
    zoom 0.5
image syq:
    "images/rw/syq.png"
    zoom 0.5
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 580
image j:
    "images/rw/jason.png"
    zoom 0.5
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 580
image canteen:
    "images/canteen/1.jpg"
    zoom 1.5
image carback:
    "images/carback.png"
    zoom 0.8
image haoxianglai:
    "images/haoxianglai.png"
    zoom 0.8
image df:
    "images/1299.png"
    zoom 0.8
image bgt:
    "images/baogaoting.png"
    zoom 0.9
image ba:
    "images/bluearchive.png"
    zoom 0.8
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 580
image kcb:
    "images/kcb.png"
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 580
    zoom 1.2
image sj:
    "images/rw/sj.png"
    zoom 0.5
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 580
image dfc:
    "images/dfc.png"
    zoom 0.82
image rx:
    "images/luckincafe.png"
    zoom 0.82
image room3:
    "images/room/room3.png"
    zoom 0.82
image wanda:
    "images/wanda/1.jpg"
    zoom 3
image yd:
    "images/wanda/4.jpg"
    zoom 3
image qqxh:
    "images/qqxh.png"
    zoom 2
image dly:
    "images/dly520.png"
    zoom 1
image glasses:
    "images/glasses.jpg"
    zoom 0.8
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 580
image kang:
    "images/kang.jpg"
    zoom 0.2
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 480
image mx1:
    "images/mx1.png"
    zoom 0.8
image mx2:
    "images/mx2.png"
    zoom 0.8

#endregion

label start:
   
    scene Sun
    with fade
    play music "audio/yinxiao/bird.wav" fadein 1.0

    "{size=45}{color=#23dae0}假期转瞬即逝，美好的休闲时光告一段落。{/size}"
    scene outschool
    with fade
    play music "audio/soft.mp3" fadein 1.0
    "2026 年 2 月 28 日，某市实验中学迎来返校日。高一学生杰森，终于等到了期盼已久的转班。"
    j "今天返校，不知道还能不能和葱哥分到一个班，唉。"
    scene classroom
    with fade
    "说着，杰森走进了十二班。看着教室里的同学，他心里一阵烦躁，提不起半点兴致。"
    cg "杰森！"
    j "葱哥！早啊。"
    "葱哥刚进教室，十二班的班主任海燕老师也走了进来。"
    hy "杰森、葱哥，你们俩被分到六班了，现在就过去吧。"
    "两人一听，顿时喜出望外，兴冲冲地奔向六班。"
    menu:
        "进入6班":
            jump game_1
    return

label game_1:

    scene classroom
    with fade
    play music "audio/soft7.mp3" fadein 1.0
    "来到六班后，杰森和葱哥坐在教室后排，班里的同学都好奇地朝他们看了过来。"
    classmate_a "后面那两个人是谁啊？"
    classmate_b "不清楚，应该是转班过来的吧。"
    "六班里有杰森以前的同学———蔡忆梦和小帕，还有上学期一起打舞萌认识的邵湛。"
    "蔡忆梦看到杰森时十分惊讶，没想到他真的转来了。"
    c "哈喽哈喽，杰森，你们俩怎么来我们班了？"
    j "当然是转班，刚好分到这儿了。"
    c "我去！你们俩真转过来了？"
    j "不然还能有假。"
    "没过多久，六班班主任树君走进了教室。"
    sj "你们两个是哪个班的？"
    j "老师，我们是从十二班转过来的。"
    sj "哦，那你们把姓名和家长电话记在我手机里，再把家庭住址、联系电话、父母姓名填到这个本子上。"
    "杰森和葱哥按要求登记完毕。随后，老师交代了开学的各项要求，收完寒假作业后，便宣布放学了。"
    menu:
        "放学":
            jump game_2
    return

label game_2:
    scene outschool
    with fade
    play music "audio/soft3.mp3" fadein 1.0

    "11点放学"

    scene carback
    with fade
    "杰森和三月七一同坐上包车。车主的女儿也在车上，后排一下子挤了四个人，从左到右依次是：车主女儿、原本同乘包车的同学、三月七、杰森。"
    "两人紧紧挨在一起，为了避免尴尬，杰森拿出手机玩起了游戏。三月七则坐在一旁，无所事事地抠着手指。自从上学期那件事之后，杰森和三月七见面便基本没有说过话。"
    scene classroom4
    with fade
    play music "audio/soft5.mp3" fadein 1.0

    "转眼就到了3月2日，正式开学的日子。开学第一天，迎接大家的自然是令人头疼的开学考。考场上的时间过得格外漫长。"
    scene classroom5
    with fade
    "杰森在考场睡了一觉又一觉，终于熬到下午四点半，考试结束。"
    scene classroom3
    with fade
    "晚上，他回到学校上晚课，和葱哥同桌坐在一起，兴致勃勃地聊着假期里的趣事。"
    menu:
        "跳过3月3日元宵节":
            jump game_3
    return

label game_3:
    scene Sun
    with fade
    play music "audio/yinxiao/bird.wav" fadein 1.0

    "元宵节一晃而过，3月4日，正式恢复正常上课。"

    scene classroom
    with fade
    play music "audio/soft7.mp3" fadein 1.0

    "来到班级，杰森发现座位被重新调整了。"
    "早上第一节就是他最不擅长的数学，曾经在七班的痛苦记忆还历历在目。"
    "直到数学老师走进教室，杰森当场傻眼，心里咯噔一下"
    j "怎么是卢丹？"
    "卢丹是年级主任，对学生管理格外严格。"
    ld "这道题，就由这一排最后一位同学来回答。"
    "话音刚落，全班的目光齐刷刷投向了杰森。"
    j "老、老师，我、我不会……"
    ld "你一点儿都不会吗？"
    "对数学选择题五分钟就能答完的杰森来说，数学老师恰好是这位严厉的主任，简直是一场噩梦。"
    "杰森沉默不语。数学课就在卢丹接连不断的提问中结束了。"
    "下课后，杰森找到邵湛，狠狠吐槽了一番卢丹，随后便开始了第二节课。"
    "六班的英语老师正是班主任树君。听完一节英语课，杰森瞬间又找回了自信。"

    scene canteen
    with fade
    play voice "audio/gfrzg.mp3" fadein 1.0
    "一天的时光转瞬即逝，不知不觉就到了午饭时间。中午依旧在小饭桌吃饭。"
    stop voice

    scene classroom
    with fade
    "下午回到学校，他的朋友小帕递给杰森一个瑞士卷，他满心感激地收下了。"
    "下午第一节课是地理，杰森实在困得忍不住睡了过去。"
    play music "audio/fight3.mp3" fadein 1.0
    
    "突然，同桌轻轻把他叫醒"
    show sj
    with fade
    "原来是树君回来了。多亏同桌及时提醒，他才侥幸躲过一劫。"
    "闲聊几句后，杰森才知道同桌名叫天宇。下午四节课一晃而过，很快就结束了。"

    scene outschool2
    menu:
        "杰森选择晚上和谁一起吃饭？"
        "邵湛":
            jump game_4
        "葱哥":
            "不行，必须跟邵湛一起吃。"
            jump game_4
    return

label game_4:
    scene haoxianglai
    with fade
    play music "audio/soft.mp3" fadein 1.0
    "杰森没有和葱哥一起去吃饭，而是跟着邵湛去了趟好想来。"
    "由于杰森要攒钱，所以他买了一个路边摊饭团，邵湛奢侈地给杰森买了瓶 AD 钙。"

    scene classroom2
    with fade
    "晚课是语文，杰森在低头写着什么，突然老师让他回答问题。"
    menu:
        "沉默":
            "杰森选择沉默，老师直接提问下一个，让他坐下了。"
            jump game_5
        "不会":
            "杰森直接说出不会，老师发怒让他写 50 遍。"
            jump game_5
    return

label game_5:
    scene classroom3
    with fade
    play music "audio/soft5.mp3" fadein 1.0
    "晚自习，由于与周围人不熟而无法聊天的杰森被一些不好的回忆笼罩了。杰森写日记给干夭讲述这一天，而他的同桌却偷看好几眼日记。他非常讨厌别人看他的日记，但是看着面露凶狠的同桌，他只好忍气吞声。"
    "虽然分了班，但是杰森在十二班养成的写日记和抄歌词的习惯还是没有改变，这是他在一个陌生的环境中唯一可以找到快乐的方式。"
    
    menu:
        "下一天":
            jump game_6

label game_6:
    scene classroom
    with fade
    play music "audio/soft3.mp3" fadein 1.0
    "杰森因为熬夜打王者荣耀，早上到学校时困得不行。"
    "走进班级，他发现树君早就到了，在还不了解老师脾气之前，他根本不敢睡觉。"
    show df
    with fade
    "杰森想起昨晚，开了一局巅峰赛，明明大顺风却被对面翻盘。玩游走的他只能无力地看着水晶爆炸，积分也从 1300 多掉到了 1299。"
    hide df
    with fade
    show kcb
    with fade
    "看着黑板上的课表，杰森发现今天有体育课，正好可以和邵湛、葱哥畅聊。"
    hide kcb
    with fade
    show ba
    "他在班里和同学们渐渐熟悉，发现这个班不像十二班那样排斥二次元。还有个叫扬帆的同学，和他一样玩《蔚蓝档案》。"
    scene classroom
    with fade
    "上午第二节是物理课，物理老师不仅年轻，身材还很瘦。"
    wlls "这个公式，杰森来背一下。"
    play music "audio/fight5.mp3" fadein 1.0
    "对物理成绩刚 “成年” 的杰森来说，这处境简直是地狱。"
    "在杰森的沉默中，老师让他站了半节课。"
    scene classroom
    with fade
    "其实他答不上来，主要是因为没有课本。他的物理书去哪了？"
    "这事要从 2 月 28 日说起。返校那天转班的他回原班取书，在十二班只领到 9 本，可实际一共 11 本，少发了两本。"
    "物理下课后，他立刻去十二班找到了纪委。"
    play music "audio/soft.mp3" fadein 1.0
    scene classroom
    with fade
    j "纪委，12班少给我发了两本书。"
    jw "哪两本?"
    j "物理必修2和英语听力必修3。"
    jw "我找找。"
    "说完，纪委在讲桌下翻找了一会儿，很快就把两本书找出来递给了他。"
    scene bgt
    with fade
    "下午学校组织去报告厅听演讲，杰森趁机美美地睡了一觉。"
    scene haoxianglai
    with fade
    "晚上，杰森又和邵湛一起去了好想来。"
    menu:
        sz "你想吃什么？"
        "拿一袋溜溜梅":
            sz "你就要一袋这个啊？行。"

        "不要":
            sz "不行，你必须要"

    scene dfc
    with fade
    "说完邵湛便付款带着杰森走出了好想来。随后邵湛买了2根淀粉肠，给杰森一根，杰森十分感激。"
    scene rx
    with fade
    sz "好想来喝瑞幸啊，我请你喝一杯吧，你看看想喝啥。"
    "说着，邵湛把手机递给杰森，杰森犹豫片刻，选了生椰拿铁。"
    menu:
        "感谢邵湛请客":
            jump game_7

label game_7:
    scene classroom3
    with fade
    play music "audio/soft5.mp3" fadein 1.0
    "晚课很快结束，到了晚自习时间。"
    sj "谁把我桌子换走了？"
    "班里一片寂静。"
    "过了一会儿"
    sj "没人承认是吧？把桌子右角露出来。"
    "查到第四个人时，他发现那位同学的桌子上有自己的标记。于是把人叫了出去，教育了一番，又让她去空教室换了张好桌子。"
    show syq
    "晚自习下课后，三月七出现在六班后门，把杰森叫了出去，却什么也没说，让人摸不着头脑。"
    scene room3
    with fade
    "晚上回到家，三月七给杰森发 QQ，炫耀她的新 “宠物”。杰森心里一阵感慨"
    j "果然，她对别人也一样动手动脚，我不过就是个过客罢了。"
    "随后他问三月七，晚自习后叫他出去到底怎么回事。"
    syq "只是路过而已。"
    j "沉默"
    "夜里杰森翻来覆去睡不着，也不知道是咖啡喝多了，还是被三月七气的。"
    menu:
        "第二天":
            jump game_8

label game_8:
    scene classroom
    with fade
    play music "audio/soft5.mp3" fadein 1.0
    "杰森早上来到班后感慨，在六班的生活比十二班强太多了。"
    scene playground
    with fade
    "上午间操，邵湛给了他一颗糖。"
    scene canteen
    with fade
    "中午杰森遇见初中同学小曲，小曲给了他一粒炫迈。"
    scene classroom2
    with fade
    "下午杰森连着睡了两节课，自习课也过得无聊至极。"

    menu:
        "做些什么？"
        "写日记":
            jump game_9
        "抄歌词":
            jump game_9

label game_9:
    scene outschool2
    with fade
    play music "audio/soft3.mp3" fadein 1.0
    "晚上杰森吃的路边摊 5 元汉堡，邵湛请了他一瓶雪碧。"
    menu:
        "坦然接受":
            pass

    scene classroom3
    with fade
    "晚课杰森坐到邵湛的旁边，和他传纸条。讲了一些杰森初中时的一些故事"
    "下课的时候葱哥找到杰森......"
    cg "杰森，过段时间我要给你个惊喜。"
    j "什么？葱哥要请我吃饭吗？"
    cg "不对，再猜猜。"
    j "难道是……"

    # 猜谜循环（猜错重来，猜对直接往下走）
    label guess_loop:
        menu:
            "鼠标":
                cg "不对再猜"
                jump guess_loop  

            "键盘":
                cg "猜对了，敬请期待吧！"
                # 正确，直接继续剧情

            "耳机":
                cg "不对再猜"
                jump guess_loop

            "手柄":
                cg "不对再猜"
                jump guess_loop

    # 猜对后会自动走到这里
    j "WC，葱哥要送我键盘！"
    "杰森心里既兴奋，又隐隐担忧，怕自己回不起同价位的礼物。"
    scene classroom3
    with fade
    "第二节晚自习，杰森跟邵湛聊起上学期他和三月七的事。"
    sz "你不就是她的舔狗吗？"
    "杰森嘴上很不服气，可仔细一想，事实好像确实如此。"
    menu:
        "忍气吞声":
            pass
        "反抗邵湛":
            sz "哈哈，死舔狗。"
    scene room3
    with fade
    "当天晚上回家后，干夭和杰森在微信上聊天。"
    yy "我喝咖啡也失眠了。"
    j "哈哈，咱俩一样，不过我是昨天失眠的。"
    menu:
        "来到三月七日":
            jump game_10
            
label game_10:
    scene classroom
    with fade
    play music "audio/soft7.mp3" fadein 1.0
    "上午化学课，杰森和葱哥被一起叫到黑板上写离子键。杰森压根没听课，只好在黑板上胡乱写了几个分子式。"
    hxls "我让你写的是离子键。"
    j "老师，我不会。"
    "他转头看向葱哥，发现葱哥不仅全都写出来了，老师还说全对。"
    "杰森早上没吃早饭，饿得有些难受，第一节课下课就去找邵湛。"
    j "邵哥，有吃的吗？"
    "邵湛从书桌里掏出一袋奥利奥递给杰森。"
    j "谢谢邵哥！"
    "因为是周六，中午休息时间很长，邵湛打算去万达出勤。"
    sz "我中午去出勤，你去吗？"
    j "可以啊，我能带葱哥吗？"
    sz "没问题。"
    scene outschool
    with fade
    "中午一放学，杰森飞奔到小饭桌打包了一份饭，就和邵湛、葱哥一起打车去了万达。"
    "邵湛不愧是有钱人，来回车费和游戏币全都他包了。"
    scene wanda
    with fade
    "到了万达，邵湛直接去了三楼的悦动游戏厅，杰森和葱哥则下楼吃饭。"
    menu:
        "杰森去了趟超市"
        "自己买一瓶饮料":
            "由于没给葱哥买，他对你的好感下降"
        "买两瓶饮料，一瓶给葱哥":
            "葱哥好感增加"
    "吃完饭后他去幸运咖买了两个冰淇淋，分别送给了葱哥和邵湛。"
    scene yd
    with fade
    "饭后他俩来到三楼。"
    j "邵哥，我请你吃个冰淇淋。"
    sz "谢了。"
    "之后杰森和邵湛玩了两次舞萌 DX，便带着葱哥打车离开了。"
    scene outschool
    with fade
    "邵湛回到学校后，去谢宝林打包了一份饭，接着就和葱哥单挑王者荣耀。"
    menu:
        "猜猜他俩谁能赢"
        "邵湛":
            "猜对，邵湛完虐葱哥"

        "葱哥": 
            "葱哥完败"
            
    scene classroom2
    with fade
    play music "audio/soft.mp3" fadein 1.0
    "下午回班上物理课，邵湛拿出筷子偷吃谢宝林，被老师当场抓包。"
    wlls "第一次见有学生上课吃东西，还敢用筷子的。"
    "在全班一片哄笑声中，邵湛直接红温了。"
    menu:
        "和同学一起笑":
            sz "你笑啥啊，杰森"
        "安慰":
            sz "我没事啊，让她说去呗。"
    scene haoxianglai
    with fade
    play music "audio/soft2.mp3" fadein 1.0
    "下午放学，杰森照旧和邵湛一起去了好想来。"
    dy "您好，加一元可以换一瓶海之言。"
    sz "来一瓶。"
    "买完后邵湛把海之言递给了杰森，杰森第一次喝，觉得味道还不错。"
    scene classroom3
    with fade
    "晚课时，邵湛的右桌康乃馨请假，杰森便偷偷挪到那个位置和他聊天。"
    "康乃馨的同桌是赵宏伟，也是杰森的初中同学。杰森晚课上左聊右聊，别提多自在了。"
    "晚自习时，杰森在日记里跟干夭感慨"
    j "我在六班比在十二班开朗了太多。"
    scene room3
    with fade
    "晚上回到家，三月七给杰森发 QQ。"
    syq "你的 QQ 号是给我了，还是借我了？"
    j "给你了。"
    syq "哦，那密码多少？"
    j "不知道，你绑下自己手机号找回密码就行。"
    syq "行"
    "随后，杰森把那个装满回忆的 QQ 小号，绑定给了三月七。"
    show qqxh
    with fade
    play music "audio/soft4.mp3" fadein 1.0
    "这个QQ小号的故事，还要从杰森初三那年说起。"
    "那时候，杰森班里来了一位转校生，是个长得十分可爱的小女孩，名叫朴欣怡"
    "她是从上海转来的——在上海，初二就已经完成了历史结业考试，所以她转来的时候，已经带着地理、生物、历史三科的中考成绩了。"
    "朴欣怡恰好坐在杰森的后面，两个人下课聊得多了，慢慢就熟络起来。"
    "杰森一时兴起，让朴欣怡下载王者荣耀，说要带她一起玩。可朴欣怡没有游戏账号，杰森便把这个QQ小号借给了她。"
    "朴欣怡接过账号后，把王者名字改成了“捕抓到一只大”。"
    "那时候的杰森，还满心以为，他和朴欣怡会一直做很好的朋友，却没料到，两人会因为一件小事彻底决裂。"
    "事情的经过是这样的：有一天，杰森像往常一样找朴欣怡双排，他特意选了云中君，想在她面前炫耀一下自己新买的皮肤，还让朴欣怡选瑶，想和她走一路。"
    "可没想到，朴欣怡一下子就生气了，还转头跟别人说杰森怪怪的，甚至造谣说杰森暗恋她。这让好面子的杰森怎么忍得了？"
    "一气之下，他直接把朴欣怡拉黑又删除，这个QQ小号也从此闲置了下来，直到去年寒假，杰森才把这个号借给了三月七。"

    menu:
        "三月八日":
            jump game_11

label game_11:

    scene dly
    with fade
    play music "audio/soft.mp3" fadein 1.0
    "今天杰森像往常一样打开王者荣耀，刚登录就看到邮件提示——邵湛送了他一个价值18.8元的朵莉亚520限定皮肤按键。"
    "杰森自从2023年买完皮肤后，就一直没舍得花钱买按键，收到这份惊喜，他立刻找到邵湛，满心感激地向他表达了谢意。"
    scene classroom
    with fade
    "转眼就到了开学日，三月九日星期一，杰森迎来了本学期的第一节微机课。"
    "出乎意料的是，这节课并没有去微机室，老师就在班里讲解了微机课的相关要求，还随机提问了一些电脑常识。"
    "杰森是个有着两年半练习时长的个人程序员，这些基础的电脑常识对他来说易如反掌，他轻松就答出了所有问题。"
    "可正是这个举动，惹怒了他的后桌李时雨——在杰森转来之前，李时雨一直是班里公认的电脑天才，而杰森的出现，彻底抢走了他的光环。"
    "李时雨心里憋着火，气得直接摔门而出。"
    "周围的同学见状，纷纷小声议论"
    someone "这下杰森死定了！李时雨肯定要找他算账。"
    "杰森听着同学们的议论，心里暗自嘀咕"
    j "我去，初中四年我都忍住没打人，难道上了高中，终于可以痛痛快快打一次了？"
    menu:
        "是否主动跟李时雨开战？"
        "打他！":
            "没打过，重新开始吧"
            return
        "不打":
            "可惜，李时雨并没有找杰森开战，而是直接请了假离开了学校。"

    "简单介绍一下李时雨吧，他是个长相十分阴柔的男生，虽然平时不常来上学，却是全年级第一。"
    scene playground
    with fade
    "转眼到了下午的体育课，自由活动时，邵湛带着杰森去了学校超市。"

    menu:
        sz "你想要喝点什么吗？"
        "不要":
            "不行，你必须要。"
        "要一瓶饮料":
            pass
    "杰森随手拿了一瓶茶萃，邵湛付完款后，直接把茶萃递给了杰森。"
    "杰森一开盖发现中了一元乐享，邵湛把饭卡给他，他又去买了一瓶。"
    scene outschool2
    with fade
    "晚上，邵湛给杰森 10 元，请他吃路边摊，杰森买了两个小鸡蛋饼。"
    scene classroom3
    with fade
    "晚课下课，杰森跟邵湛聊天，聊到了干夭，让康乃馨听到了。"
    knx "你们说的是那个白白的，可可爱爱的小干夭吗？"
    j "我去，你竟然认识他啊？"
    knx "他是我小学同学，小学时他小小的很可爱。"
    j "他是我初中最好的兄弟，要加个 VX 吗？我有他初中的照片。"
    knx "好啊。"
    "晚上杰森加了康乃馨的 VX，给他发了几张干夭的照片。"

    menu:
        "三月十日":
            jump game_12

label game_12:

    scene canteen
    with fade
    play music "audio/soft7.mp3" fadein 1.0

    "早上第二节下课，邵湛带着杰森去食堂买鸡腿，偶遇一个杰森的兄弟韩子瑶。"
    j "韩姐，你这眼镜挺帅啊。"

    scene playground
    with fade
    show glasses
    "韩子瑶把一个很酷的墨镜借给了杰森，杰森上体育课一戴，回头率可高了。"

    scene classroom2
    with fade
    "下午自习课，杰森迎来了新座，他的新同桌叫刘昊，外号 “大仙”。"
    "刘昊从串完座开始就一直跟杰森吹牛逼。"
    xian "我初中的时候，被 3 个大汉包围，我先给最前的人一脚，然后掏出小刀，解决了另外两个人。"
    menu:
        "不信":
            j "大仙真能吹牛逼"
            "被刘昊打一顿"
        "信":
            j "大仙牛逼"
            "刘昊很开心，继续和杰森吹牛逼。"
    "晚课刘昊跟杰森聊嗨了。"
    xian "给你 10 块钱，你以后就是我兄弟了。"
    menu:
        "收下":
            j "谢谢大仙"
            "刘昊继续和杰森吹牛逼。"
        "拒绝":
            j "大仙，我不要"
            xian "不行你必须收下"
    "晚自习，杰森盯着墙上的照片发呆，这些照片是上学期六班同学拍的。"
    show kang
    with fade
    "他看到一张长得很好看的女生的照片，于是问刘昊她是谁？"
    xian "不知道啊，可能是别的班的吧。"
    "下课后，杰森跟邵湛说那张照片，邵湛笑着说"
    hide kang
    with fade
    sz "那张是康乃馨啊！她之前朋友圈发过。"
    j "什么？那是康乃馨？"
    "杰森难以置信的看向康乃馨，不论是肤色还是发型都不一样啊！"
    "杰森内心感慨：有种像网恋奔现的感觉。"

    menu:
        "三月十一日":
            jump game_13

label game_13:

    scene classroom
    with fade
    play music "audio/soft.mp3" fadein 1.0

    "杰森今天上课发呆的时候突然发现，班里男生和男生一座，女生和女生一座。"
    j "这种排座让多少人羡慕啊！跟同性人当同桌说话不用顾及。"

    scene bgt
    with fade
    play music "audio/soft2.mp3" fadein 1.0

    "下午自习课，学校在报告厅举行了开学典礼，有六个主持人，其中有两位是杰森的初中同学。"
    "杰森跟邵湛聊了 2 个小时，直到活动结束。"

    scene outschool2
    with fade
    "晚上杰森花 8 元买了盒路边的盒饭"
    scene mx2
    with fade
    "然后去蜜雪冰城吃，那个饭不能用难吃来形容，只能说是难吃的要死。"
    show syq
    "在 17:10 的时候，杰森在蜜雪冰城看到了两个熟悉的面孔，张依依和三月七。"
    "见到杰森以后依旧互不搭理，像陌生人一样。"
    hide syq
    "说实话，三月七不理杰森一定是因为张依依在背后说什么了，要不然不可能变成现在这样，两个最熟悉的人相见犹如陌生人。"
    scene classroom3
    with fade
    "晚二下课，杰森借到小帕的绳子绑在了腿上，充当腿环。"
    "晚自习杰森一直在发呆，做些什么？"
    menu:
        "写日记":
            jump game_14
        "抄歌词":
            jump game_14

label game_14:

    scene haoxianglai
    with fade
    play music "audio/soft5.mp3" fadein 1.0

    "中午杰森来到超市，打算为干夭准备实验中学特产，粉色魔爪。"
    "杰森买了三瓶，分别送给了葱哥和邵湛，干夭的会在两天后的周六送给他。"
    scene mx2
    with fade
    "买完饮料后，杰森来到蜜雪冰城，看邵湛帮他打王者上星。"
    show df
    "杰森发现自己的王者师傅在线，于是让邵湛把他拉进来一起玩。"
    "开局邵湛秒选了一个小乔大王，16/0 顶级中路，带飞全场。"
    scene classroom
    with fade
    "中午回班的时候，杰森又遇到了三月七，双方依旧视而不见，犹如陌生人。"
    scene classroom2
    "下午第二节课，老师去开会了，杰森在班里"
    menu:
        "写日记":
            "记录了一下美好生活"
        "抄歌词":
            "抄了一些好听的歌词。"
        "睡觉":
            "睡了半节课，精神了不少"
    scene outschool2
    with fade
    "晚上杰森吃了个路边摊 5 元小汉堡，邵湛送给杰森一袋奥利奥。"
    scene classroom3
    with fade
    "晚课生物，班长的同桌单桐桐喝了三瓶 RIO 强爽，杰森羡慕死了。"
    "晚三杰森的前同桌天宇睡觉打呼噜了，被树君录视频发给他妈了。"

    menu:
        j "2026年8月17日21点02分，今天就更新到这里吧！我累了！还剩4页剧情我上学期写的剧情就没了。"
        "敬请期待":
            $ OpenURL("https://www.bigjackson.vip/game")()
        "退出游戏":
            jump exit

label exit:
    "未完待续..."
return
