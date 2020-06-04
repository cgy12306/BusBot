import requests

def lambda_function(event, context):
    cnt=0
    arr=[]
    tmarr=[]
    res = requests.get(url="http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?serviceKey=5lit2mR%2BPSUj1pJ5DXYFDFoo7SeSjYrH51FjJtguiH28Me%2Byk2Fw7KpUoDdNq3AIr50OGWi%2FevpQlQ7Y%2FRsBSg%3D%3D&stId=118000185&busRouteId=115000007&ord=67")

    test = res.text
    while True:
        if '/' in test:
            arr.append(test.split('/'))
        if 'stationNm1' in arr[0][cnt]:
            first=arr[0][cnt]
            second=arr[0][cnt+1]


            f=first.split('<')
            s=second.split('<')
            
            first_station=f[1].split('>')[1]
            second_station=s[1].split('>')[1]

            break
        cnt+=1
        
    while True:
        if 'arrmsg' in test:
            tmarr.append(test.split('arrmsg')[1])
            tmarr.append(test.split('arrmsg')[3])
            t1=tmarr[0].split('>')[1]
            t2=tmarr[1].split('>')[1]

            first_time=t1.split('<')[0]
            second_time=t2.split('<')[0]
            print(first_time, second_time)
        break

    response = {
        "text": "구로역행 대림역 버스 정류소 정보입니다.",
        "attachments": []}

    response['attachments'].append({"text" : f"{first_station} - {first_time}    {second_station} - {second_time}"})
    
    #response['attachments'].append("text" : f"{second_station}")
    #response['attachments'].append({"text": f"{first_station} ({first_time}) - {second_station}"})
    return(response)

if __name__ =="__main__": # 터미널에서만 실행시켜라라는 뜻
    print(lambda_function(None, None))
