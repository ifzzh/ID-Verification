import json
import openpyxl

fp = open('./归属地.json','r',encoding='utf8')
area_dict = json.load(fp)



def checkArea(areaId):
    '''校验地区。输入6位地区编码字符串，返回：{code, id, {province, city, district, note}}'''
    if len(areaId) != 6:
        return {'code': 'Error', 'id': areaId, 'area': '区域码长度需要为6位'}
    if areaId.isdigit() == False:
        return {'code': 'Error', 'id': areaId, 'area': '非法区域码'}
    if areaId in area_dict:
        return {'code': 'OK', 'id': areaId, 'area': {'province': area_dict[areaId]['p'], 'city': area_dict[areaId]['a'], 'district': area_dict[areaId]['d'], 'note': area_dict[areaId]['i']}}
    else:
        return {'code': 'Error', 'id': areaId, 'area': '未知区域码'}
    
# if __name__ == '__main__':
#     print(checkArea('110000')) # 北京市
#     print(checkArea('130000')) # 河北省
#     print(checkArea('130100')) # 石家庄市