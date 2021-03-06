OKONOMIYAKI_MENU = {
    'Aメニュー': {'もち', '明太子', '豚肉'},
    'Bメニュー': {'キムチ', '明太子', '牛肉'},
    'Cメニュー': {'チーズ', '天かす', '牛肉'},
    'Dメニュー': {'もち', 'チーズ', 'イカ'},
}


def output_complement_menu(want_to_eat):
    """食べたいお好み焼きの具がどのメニューに含まれているか出力します"""
    #for menu_name, gu_set in OKONOMIYAKI_MENU.items():
        # ここにメニューの部分集合演算を書く
    gu_set={'チーズ','豚肉'}
    menu_name='Aメニュー'
    gu_issubset = want_to_eat <= gu_set # 食べたいものが全て含まれている
        # ここにメニューの 積集合演算を書く
    gu_intersection =  want_to_eat & gu_set # 一部、食べたいものが含まれる
    print(gu_intersection)
    if gu_issubset:
            # 食べたい具が全て含まれている場合
        print('{}に食べたい具がすべて揃っています：{}'.format(menu_name, gu_set))
    elif gu_intersection:
            # 食べたい具が全て含まれているメニューがない場合、既存のメニューにトッピングすることにします。
        print('{}に食べたい具が一部あります：{}'.format(menu_name, gu_intersection))
            # ここにメニューの差集合演算を書く
        additional_topping = want_to_eat - gu_set
        print('  追加トッピングは{}です'.format(additional_topping))
    else:
        print('{}には、食べたい具が含まれません'.format(menu_name))


def main():
    want_to_eat = {'明太子', 'イカ'}
    print('食べたい具: {}'.format(want_to_eat))

    output_complement_menu(want_to_eat)


if __name__ == '__main__':
    main()
