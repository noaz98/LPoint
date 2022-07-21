# 카테고리에 속한 상품코드 찾는 함수 생성
def find_item_cod(item_list, item_cod):
    for i in item_list:
        for j in i.values():
            if item_cod in j:
                result = [k for k, v in i.items()]
                return result


