#encoding=utf-8

import os
import sys

def checkAns(outputFile1, outputFile2):
	"""
		璇ュ嚱鏁扮敤浜庡垽鏂袱涓緭鍏ユ枃浠舵槸鍚︾浉鍚岋紝杩欓噷閲囩敤鐨勬柟寮忔槸璇诲叆涓や釜鏂囦欢鐨勬墍鏈夎锛岀劧鍚庢嫾璧锋潵鍒ゆ柇鏄惁鐩稿悓銆傚彲浠ユ牴鎹渶姹備慨鏀�
		outputFile1,outputFile2 鍒嗗埆涓哄垽鏂殑涓や釜鏂囦欢鐨勬枃浠跺悕
		鍑芥暟杩斿洖甯冨皵鍊�
	"""
	with open(outputFile1, "r") as f:
		output1 = f.readlines()
	with open(outputFile2, "r") as f:
		output2 = f.readlines()
	return "".join(output1) == "".join(output2)

if len(sys.argv) - 1 != 3:
	sys.stdout.write("Usage: %s <program1> <program2> <datamaker>\n" % sys.argv[0])
	sys.stdout.write("    Example on Linux: python3 %s ./a \"python3 b.py\" \"python3 datamaker.py\"\n" % sys.argv[0])
	sys.stdout.write("    Example on Windows: python3 %s a.exe \"python3 b.py\" \"python3 datamaker.py\"\n" % sys.argv[0])
	exit(1)

cnt = 0
while True:
	cnt += 1
	sys.stdout.write("Running Case #%s ... " % cnt)
	if 0 != os.system("%s > input.txt" % sys.argv[3]):
		sys.stdout.write("Run datamaker failed\n")
		break
	if 0 != os.system("%s < input.txt > output1.txt" % sys.argv[1]):
		sys.stdout.write("Run program1 failed\n")
		break
	if 0 != os.system("%s < input.txt > output2.txt" % sys.argv[2]):
		sys.stdout.write("Run program2 failed\n")
		break
	if not checkAns("output1.txt", "output2.txt"):
		sys.stdout.write("Wrong\n")
		break
	sys.stdout.write("OK\n")
