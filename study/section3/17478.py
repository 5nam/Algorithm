n = int(input())

def printUnderBar(lev):
	print("_" * (lev*4), end="")

def func(lev):
	global s1, s2, s3, s4, s5

	printUnderBar(lev)
	print(s1)

	# base case
	if lev == n:
		printUnderBar(lev)
		print(s2)
		printUnderBar(lev)
		print(s3)
		return

	# recursive case
	printUnderBar(lev)
	print(s4)
	printUnderBar(lev)
	print(s5)
	printUnderBar(lev)
	print(s6)
	func(lev+1)
	printUnderBar(lev)
	print(s3)

s0 = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
s1 = "\"재귀함수가 뭔가요?\""
s2 = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
s3 = "라고 답변하였지."
s4 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
s5 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
s6 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""

print(s0)
func(0)