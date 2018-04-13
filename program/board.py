def add(a, b): return tuple(map(lambda d: d[0] + d[1], zip(a, b)))

class Board:
	def __init__(self, s):
		self.program = list(filter(lambda s: s != '', s.split("\n")))
		self.instruction_pointer = self.get_start(self.program)
		self.pointer_velocity = (1, 0)
		self.run()

	def run(self):
		stack = []
		token = ""
		reading = False
		Running = True
		while Running:
			self.instruction_pointer = add(self.instruction_pointer,
										   self.pointer_velocity)

			if self[self.instruction_pointer] == ">":
				self.pointer_velocity = add(self.pointer_velocity, (1, 0))
			elif self[self.instruction_pointer] == "<":
				self.pointer_velocity = add(self.pointer_velocity, (-1, 0))
			elif self[self.instruction_pointer] == "^":
				self.pointer_velocity = add(self.pointer_velocity, (0, -1))
			elif self[self.instruction_pointer] == "\\":
				self.pointer_velocity = add(self.pointer_velocity, (0, 1))
			elif self[self.instruction_pointer] == "#":
				reading = True
			elif self[self.instruction_pointer] == "?":
				reading = False
				stack.append(eval(token))
				token = ""
			elif self[self.instruction_pointer] == "|":
				print(stack.pop())
			elif self[self.instruction_pointer] == "&":
				a = stack.pop()
				stack.append(a)
				stack.append(a)
			elif self[self.instruction_pointer] == "+":
				stack.append(stack.pop() + stack.pop())
			elif self[self.instruction_pointer] == "-":
				stack.append(stack.pop() - stack.pop())
			elif self[self.instruction_pointer] == "*":
				stack.append(stack.pop() * stack.pop())
			elif self[self.instruction_pointer] == "/":
				stack.append(stack.pop() / stack.pop())
			elif self[self.instruction_pointer] == ":":
				self.pointer_velocity = (self.pointer_velocity[0], 0)
			elif self[self.instruction_pointer] == ";":
				self.pointer_velocity = (0, self.pointer_velocity[1])
			elif self[self.instruction_pointer] == "@":
				Running = False
			else:
				if reading:
					token += self[self.instruction_pointer]


	def get_start(self, program):
		for y, line in enumerate(program):
			for x, column in enumerate(line):
				if column == "~":
					return (x, y)

		raise Exception('No entry point.')

	def __getitem__(self, d):
		# print(self.program[d[1]%(len(self.program))][d[0]%(len(self.program[0]))])
		return self.program[d[1]%(len(self.program))][d[0]%(len(self.program[d[1]%(len(self.program))]))]