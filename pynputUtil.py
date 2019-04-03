## 监听键盘
from pynput.keyboard import Key, Listener,KeyCode,Controller
import pyperclip
import time

class pynputUtil(object):
	"""docstring for pynputUtil"""
	def __init__(self):
		super(pynputUtil, self).__init__()
		self.shift = False
		self.ctrl = False
		self.alt = False
		self.recordPath = 'record.txt'
		# 连接事件以及释放
		with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
			print("开始监听键盘输入")
			listener.join()
	def on_press(self,key):
		print('{0} release'.format(key))
		if key == Key.ctrl_l:
			self.ctrl = True
		elif self.ctrl:
			# print("ctrl+{0}".format(key))
			if key == KeyCode.from_char('c'):
				self.ctrl = False
				info = pyperclip.paste()
				curtime = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
				info = '时间：{0} \n {1} \n'.format(curtime,info)
				print(info)
				with open(self.recordPath, 'a+',encoding='gbk',errors='ignore') as f:
					f.write(info)
		# if key == Key.ctrl:
		# 	self.ctrl = True
		# elif self.ctrl:
		# 	print("ctrl+{0}".format(key)
		# if key == Key.alt:
		# 	self.alt = True
		# elif self.alt:
		# 	print("alt+{0}".format(key))
	def on_release(self,key):
		# 监听释放
		# print('{0} release'.format(key))
		self.ctrl = False
		if key == Key.esc:
			# Stop listener
			return False
def main():
	pyn = pynputUtil()
if __name__ == "__main__":
	main()
