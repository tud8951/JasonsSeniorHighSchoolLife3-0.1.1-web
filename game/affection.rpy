# ==============================
# 好感度系统 · 说明页100%不遮挡版
# ==============================

default shao_zhan = 62
default cong_ge = 82
default cai_yimeng = 42
default tian_yu = 55
default wallet = 100

init python:
    if not hasattr(store, 'shao_zhan'):
        store.shao_zhan = 62
    if not hasattr(store, 'cong_ge'):
        store.cong_ge = 82
    if not hasattr(store, 'cai_yimeng'):
        store.cai_yimeng = 42
    if not hasattr(store, 'tian_yu'):
        store.tian_yu = 55
    if not hasattr(store, 'wallet'):
        store.wallet = 100

# 基础样式
style hpanel_frame:
    xsize 720
    ysize 560
    background "#121212e6"
    padding (40, 36)
    align (0.5, 0.5)

style h_title_text:
    size 32
    color "#f7f7f7"
    bold True

style h_name_text:
    size 24
    color "#ffffff"
    bold True

style h_value_text:
    size 20
    color "#cccccc"

style h_bar:
    xsize 280
    ysize 26
    left_bar "#ff87b8"
    right_bar "#33333333"

style h_button_frame:
    padding (18, 10)
    background "#333333cc"

# 统一按钮样式
style h_close_button:
    padding (24, 12)
    background "#ff5c7a"
    color "#ffffff"
    bold True
    xsize 180

style h_help_button:
    padding (24, 12)
    background "#4a86e8"
    color "#ffffff"
    bold True
    xsize 180

style h_cg_main_button:
    padding (24, 12)
    background "#ff88bb"
    color "#ffffff"
    bold True
    xsize 180

# CG按钮样式
style h_cg_select_button:
    padding (20, 14)
    background "#333333"
    color "#ffffff"
    bold True
    xsize 420
    hover_background "#555555"

screen affection_button():
    frame style "h_button_frame":
        xalign 0.5
        yalign 0.96
        textbutton "好感度" action Show("affection_panel") text_size 22 text_color "#ffffff"

# 好感度主面板
screen affection_panel():
    modal True
    add "#00000090"

    frame style "hpanel_frame":
        text "角色好感度" style "h_title_text" align (0.5, 0.08)

        hbox:
            xalign 0.5
            ypos 0.20
            spacing 60

            # 左列
            vbox spacing 30:
                vbox spacing 8:
                    text "邵湛" style "h_name_text"
                    bar value shao_zhan range 100 style "h_bar"
                    text "好感：[shao_zhan] / 100" style "h_value_text"

                vbox spacing 8:
                    text "葱哥" style "h_name_text"
                    bar value cong_ge range 100 style "h_bar"
                    text "好感：[cong_ge] / 100" style "h_value_text"

                vbox spacing 8:
                    text "钱包" style "h_name_text"
                    bar value wallet range 100 style "h_bar"
                    text "数值：[wallet] / 100" style "h_value_text"

            # 右列
            vbox spacing 30:
                vbox spacing 8:
                    text "蔡忆梦" style "h_name_text"
                    bar value cai_yimeng range 100 style "h_bar"
                    text "好感：[cai_yimeng] / 100" style "h_value_text"

                vbox spacing 8:
                    text "天宇" style "h_name_text"
                    bar value tian_yu range 100 style "h_bar"
                    text "好感：[tian_yu] / 100" style "h_value_text"

        # 底部按钮组
        hbox:
            xalign 0.5
            ypos 0.87
            spacing 20

            textbutton "CG" action Show("cg_select_screen") style "h_cg_main_button"
            textbutton "说明" action Show("affection_help") style "h_help_button"
            textbutton "关闭" action Hide("affection_panel") style "h_close_button"

# CG选择界面
screen cg_select_screen():
    modal True
    add "#000000dd"

    frame:
        xsize 720
        ysize 600
        xalign 0.5
        yalign 0.5
        background "#111111f0"
        padding (40, 40)

        text "角色好感度 CG 鉴赏" style "h_title_text" xalign 0.5 ypos 0.05

        vbox:
            xalign 0.5
            ypos 0.2
            spacing 20

            textbutton "邵湛 CG" action If(shao_zhan >= 100, Jump("cg_shao_zhan"), Call("cg_locked")) style "h_cg_select_button"
            textbutton "葱哥 CG" action If(cong_ge >= 100, Jump("cg_cong_ge"), Call("cg_locked")) style "h_cg_select_button"

        textbutton "返回" action Hide("cg_select_screen") style "h_close_button" xalign 0.5 ypos 0.93

# ======================
# ✅ 这里是修复后的说明页（绝对不遮挡）
# ======================
screen affection_help():
    modal True
    add "#000000cc"

    frame style "hpanel_frame":
        text "好感度说明" style "h_title_text" xalign 0.5 ypos 0.05
        
        # 文字整体大幅上移，永远碰不到按钮
        vbox:
            xalign 0.5
            ypos 0.12   # 上移到最顶部
            spacing 16
            
            text "· 好感度是杰森对他人的好感度" color "#ffffff" size 20
            text "· 选择不同选项会影响角色好感" color "#ffffff" size 20
            text "· 0-20：陌生" color "#cccccc" size 18
            text "· 21-40：熟悉" color "#88ccff" size 18
            text "· 41-60：友好" color "#ffcc88" size 18
            text "· 61-80：信赖" color "#ffcc88" size 18
            text "· 81-90：亲密" color "#ffcc88" size 18
            text "· 91-100：挚爱" color "#ff88bb" size 18
            text "· 钱包是杰森的财产" color "#ffffff" size 20
            text "· 当钱包等于0时，杰森会破产" color "#ff0000" size 18

        # 返回按钮放到最最底部，完全隔离
        textbutton "返回" action Hide("affection_help") style "h_close_button" xalign 0.5 ypos 0.96

# 好感逻辑
init python:
    def add_affection(char, value):
        if char == "shao_zhan":
            store.shao_zhan = max(0, min(100, store.shao_zhan + value))
        elif char == "cong_ge":
            store.cong_ge = max(0, min(100, store.cong_ge + value))
        elif char == "cai_yimeng":
            store.cai_yimeng = max(0, min(100, store.cai_yimeng + value))
        elif char == "tian_yu":
            store.tian_yu = max(0, min(100, store.tian_yu + value))
        elif char == "wallet":
            store.wallet = max(0, min(100, store.wallet + value))

    def set_affection(char, value):
        if char == "shao_zhan":
            store.shao_zhan = max(0, min(100, value))
        elif char == "cong_ge":
            store.cong_ge = max(0, min(100, value))
        elif char == "cai_yimeng":
            store.cai_yimeng = max(0, min(100, value))
        elif char == "tian_yu":
            store.tian_yu = max(0, min(100, value))
        elif char == "wallet":
            store.wallet = max(0, min(100, value))

# ==============================
# CG 场景
# ==============================
label cg_shao_zhan:
    hide screen cg_select_screen
    show cg_shao_zhan with fade
    "你观看了邵湛的专属CG。"
    pause
    hide cg_shao_zhan with fade
    return

label cg_cong_ge:
    hide screen cg_select_screen
    show cg_cong_ge with fade
    "你观看了葱哥的专属CG。"
    pause
    hide cg_cong_ge with fade
    return

label cg_locked:
    "该角色好感度不足，无法查看CG。"
    return

# # 天宇好感 +10
# $ add_affection("tian_yu", 10)

# # 直接设置天宇好感为 70
# $ set_affection("tian_yu", 70)