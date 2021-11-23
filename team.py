from bs4 import BeautifulSoup
import urllib.request
import re
import team_if_work

title_list = ["1.토공사", "2.기초공사", "3.골조공사", "4.조적공사", "5.미장공사", "6.방수공사", "7.지붕공사", "8.창호공사", "9.도장공사"]

print("-"*20, "공종 목록", "-"*20)
for title in title_list:
    print(title)
print("-"*20, "공종 선택", "-"*20)
type = map(int, input("수행하는 공종을 선택해주세요. >>> ").split())
print("\n")


print('-오늘의 날씨-')
webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B3%B5%EB%A6%89%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EB%8F%84%EB%8B%B4%EB%8F%99+%EB%82%A0%EC%94%A8&tqi=hiLhCsp0JXVssdi3iGossssssuR-100634/')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('div', "temperature_text")
# humidity = soup.find('dl', "summary_list")
humidity = soup.select('dd.desc')
temperature = temps.get_text()
hum = humidity[1].get_text()
rain = humidity[0].get_text()
new_tem = int(re.sub(r"[^a-zA-Z0-9]", "", temperature))
new_hum1 = int(re.sub(r"[^a-zA-Z0-9]", "", hum))
new_hum2 = int(re.sub(r"[^a-zA-Z0-9]", "", rain))

print('--> 날씨 : ', temperature)
print('--> 습도 : ',  hum)
print('--> 강수확률 : ', rain)
print("\n")

for num in type:
    team_if_work.work_instruction(num)
    print("-"*50)
    #
    # if num == 9:
    #     paint(new_tem, new_hum1, new_hum2)
    #
    # elif num == 6:
    #     water_proof(new_tem, new_hum1, new_hum2)
    #

'''
def water_proof(tem, hum, rain):
    if new_tem > 10:
        print("방수공사 하기 적합한 환경입니다.")


def paint(tem, hum, rain):
    if new_tem < 15:
        print("도장공사 하기 적합한 환경입니다.")
'''
