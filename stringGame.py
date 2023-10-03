# 사용자가 입력한 문자열 값에 따라 사칙연산을 수행할 수 있는 계산기를 구현해야 한다.
# 문자열 계산기는 사칙연산의 계산 우선순위가 아닌 입력 값에 따라 계산 순서가 결정된다. 즉, 수학에서는 곱셈, 나눗셈이 덧셈, 뺄셈 보다 먼저 계산해야 하지만 이를 무시한다.
# 예를 들어 "2 + 3 * 4 / 2"와 같은 문자열을 입력할 경우 2 + 3 * 4 / 2 실행 결과인 10을 출력해야 한다.
# 사용자가 입력한 연산식이 올바르지 않은 경우 IllegalArgumentException 을 발생시킨다. 단, 프로그램이 죽어선 안된다.
# IllegalArgumentException 에러가 발생 했을 때 사용자에게 올바른 연산식이 아닙니다 라는 문구를 포함한 내용을 콘솔창에 표출해야 한다.

class Cal:
    @staticmethod
    def calculate(_str):
        try:
            result = eval(_str)  # 문자열을 평가하여 계산
            return result
        except ZeroDivisionError:
            raise ValueError("0으로 나눌 수 없습니다.")
        except Exception as e:
            raise ValueError("올바른 연산식이 아닙니다. 에러: " + str(e))


if __name__ == '__main__':

    _str = input("사칙연산식을 입력하세요: ")

    try:
        result = Cal.calculate(_str)
        print("결과:", result)
    except ValueError as ve:
        print("오류:", str(ve))

