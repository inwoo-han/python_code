import random

class upgrade_Simul:
    input_menu = 0                  # 메뉴 선택
    #nor_lv = 0                      # 일반 모드의 강화 단계 삭제
    ug_try_cnt = 0                  # 강화 시도 횟수
    #cus_lv_input = 0                # 커스텀 메뉴 강화 단계 삭제
    ug_chk = 0                      # 강화 시작 여부
    per_success = [1000, 1000, 1000, 1000, 1000, 600, 450, 300,
                   300, 300, 150, 150, 150, 100, 100, 100, 50, 50, 30, 30, 10, 10, 5, 5] # 단계별 강화 확률
    #per_success = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
    #               1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
    per_wei_success = 0.0           # 강화 누적성공 확률
    try_cnt = 0                     # 강화 시도 횟수
    fail_cnt = 0                    # 강화 실패 횟수
    jangin = 0.0                    # 장인의 기운
    per_weight = 0                  # 강화 확률 누적 증가
    # need_material = 0               # 소모 재화
    # wei_material = 0                # 누적 소모 재화
    ug_lv = 0                       # 강화 수치
    ug_result = ''                  # 강화 결과
    randNum = 0                     # 랜덤 뽑기(확률)

    #randNum = random.randrange(1,1000) 랜덤뽑기로 확률 산출

    '''def menu_chk(self):
        print('메뉴를 선택해주세요.')
        print('-1 종료, 1 일반모드, 2 커스텀모드')
        self.input_menu = int(input('입력 : '))
        if self.input_menu == -1:
            quit()
        elif self.input_menu == 1:
            self.nor_mode()
        elif self.input_menu == 2:
            self.cus_mode()
        return self.input_menu'''

    def reset_var(self):
        self.input_menu = 0  # 메뉴 선택
        self.ug_try_cnt = 0  # 강화 시도 횟수
        self.ug_chk = 0  # 강화 시작 여부
        self.per_success = [1000, 1000, 1000, 1000, 1000, 600, 450, 300,
                       300, 300, 150, 150, 150, 100, 100, 100, 50, 50, 30, 30, 10, 10, 5, 5]  # 단계별 강화 확률
        self.per_wei_success = 0.0  # 강화 누적성공 확률
        self.try_cnt = 0  # 강화 시도 횟수
        self.fail_cnt = 0  # 강화 실패 횟수
        self.jangin = 0.0  # 장인의 기운
        self.per_weight = 0  # 강화 확률 누적 증가
        self.ug_lv = 0  # 강화 수치
        self.ug_result = ''  # 강화 결과
        self.randNum = 0  # 랜덤 뽑기(확률)

    def nor_mode(self):
        print('일반모드 시작')
        self.reset_var()
        self.ug_lv = 1
        self.per_wei_success = self.per_success[self.ug_lv - 1]
        #self.upgrade_start()
        return self.ug_lv, self.per_wei_success

    def cus_mode(self, ug_lv):
        print('커스텀모드 시작')
        # self.jangin = 0.0
        # self.fail_cnt = 0
        self.reset_var()
        self.ug_lv = ug_lv
        self.per_wei_success = self.per_success[self.ug_lv - 1]
        return self.ug_lv, self.per_wei_success

    def upgrade_start(self):
        try:
            # self.per_wei_success = self.per_success[self.ug_lv - 1]
            print('강화레벨 :', self.ug_lv)                         # 현재 강화 확률 출력
            print('성공확률 :', round(self.per_wei_success * 0.1, 2), '%')   # 성공 확률 출력
            # self.ug_chk = int(input('강화시작(1입력) : '))
            print('-' * 30)                                     # 구분선 출력
            self.randNum = random.randrange(1, 1000)            # 0.1% 확률까지 가능하게 하기 위해 1000
            print(self.randNum)

            if self.per_wei_success >= self.randNum or self.jangin >= 1000:  # 강화 성공시 수행
                self.ug_result = '강화 성공'
                print(self.ug_result)
                if self.jangin >= 1000:
                    print('장인의 기운 성공')
                self.ug_lv += 1
                self.try_cnt += 1
                print('현재 단계 실패 횟수 :', self.fail_cnt)
                print('총 시도 횟수 :', self.try_cnt)
                print('-' * 30)
                self.jangin = 0                                 # 성공 시 장인의 기운 초기화
                self.fail_cnt = 0                               # 성공 시 실패 횟수 초기화
                self.per_wei_success = self.per_success[self.ug_lv-1]  # 성공 시 다음 레벨 강화 확률
                # print('성공확률 : ', self.per_wei_success * 0.1, '%')

            elif self.per_wei_success < self.randNum:                       # 강화 실패시 수행
                if self.fail_cnt < 10:
                    self.fail_cnt += 1
                    self.per_wei_success = self.per_success[self.ug_lv-1] + (self.per_success[self.ug_lv-1] * (self.fail_cnt * 0.1))
                else:
                    self.fail_cnt += 1
                self.ug_result = '강화 실패'
                print(self.ug_result)
                print('현재 단계 실패 횟수 :', self.fail_cnt)
                self.try_cnt += 1
                print('총 시도 횟수 :', self.try_cnt)
                self.jangin += (self.per_wei_success * 0.465)
                print('장인의 기운 : ', round(self.jangin * 0.1, 3), '%')
                print('성공확률 : ', round(self.per_wei_success * 0.1, 2), '%')
                print('-' * 30)

            print(self.ug_result, self.ug_lv)
            return self.ug_result, self.ug_lv, self.per_wei_success, self.fail_cnt, self.jangin  # 파이게임에서 보여줄 강화 결과와 강화 단계
        except IndexError as e:                         # 강화 최대치 달성 시 리스트 범위를 벗어나게 되어 IndexError 에러 발생을 이용해 강화 최대치임을 알려준다.
            print("강화 최대치 입니다! 축하합니다!", e)
        except Exception as e:
            print("오류발생 :", e)



#ug = upgrade_Simul()
#ug.upgrade_start()
#ug.menu_chk()
