from winsound import Beep


import time

def freq(o, s):
    if s == '도':     return 524*2**o
    elif s == '도샾': return 554*2**o
    elif s == '레':   return 587*2**o
    elif s == '레샾': return 622*2**o
    elif s == '미':   return 659*2**o
    elif s == '파':   return 698*2**o
    elif s == '파샾': return 740*2**o
    elif s == '솔':   return 784*2**o
    elif s == '솔샾': return 831*2**o
    elif s == '라':   return 880*2**o
    elif s == '라샾': return 932*2**o
    elif s == '시':   return 988*2**o




# Beep(freq(0,'솔'),500)
# Beep(freq(0,'솔'),500)
# Beep(freq(0,'라'),500)
# Beep(freq(0,'라'),500)
# Beep(freq(0,'솔'),500)
# Beep(freq(0,'솔'),500)
# Beep(freq(0,'미'),500)
# time.sleep(0.5)
# Beep(freq(0,'솔'),500)
# Beep(freq(0,'솔'),500)
# Beep(freq(0,'미'),500)
# Beep(freq(0,'미'),500)
# Beep(freq(0,'레'),500)
# time.sleep(0.5)
# Beep(freq(0,'솔'),500)
# Beep(freq(0,'솔'),500)
# Beep(freq(0,'라'),500)
# Beep(freq(0,'라'),500)
# Beep(freq(0,'솔'),500)
# Beep(freq(0,'솔'),500)
# Beep(freq(0,'미'),500)
# time.sleep(0.5)
# Beep(freq(0,'솔'),500)
# Beep(freq(0,'미'),500)
# Beep(freq(0,'레'),500)
# Beep(freq(0,'미'),500)
# Beep(freq(0,'도'),500)



t=700
d = 80
Beep(freq(1,'도'),int(1*t)-d) #암
Beep(freq(1,'도샾'),int(0.5*t)-d) #욜
Beep(freq(1,'도샾'),int(1*t)-d) #맨
Beep(freq(0,'솔샾'),int(0.5*t)-d) #암
Beep(freq(0,'솔샾'),int(0.5*t)-d) #욜
Beep(freq(1,'도샾'),int(0.5*t)-d) #맨
Beep(freq(1,'도샾'),int(0.5*t)-d) #그
Beep(freq(1,'레샾'),int(0.5*t)-d) #대
Beep(freq(1,'도샾'),int(1*t)-d) #여
time.sleep((t*0.5-d)/1000) # 쉬고
Beep(freq(0,'솔샾'),int(0.25*t)-d) #다
Beep(freq(0,'솔샾'),int(0.25*t)-d) #라
Beep(freq(0,'솔샾'),int(0.25*t)-d) #다
Beep(freq(1,'도샾'),int(0.25*t)-d) #따
Beep(freq(1,'도샾'),int(0.5*t)-d) #오
Beep(freq(0,'시'),int(0.5*t)-d) #늘
Beep(freq(1,'도샾'),int(1*t)-d) #도
time.sleep((t*0.75-d)/1000) # 쉬고
Beep(freq(1,'도샾'),int(0.25*t)-d) #나
Beep(freq(1,'도샾'),int(0.25*t)-d) #는
Beep(freq(1,'도샾'),int(0.5*t)-d) #오
Beep(freq(1,'도샾'),int(0.5*t)-d) #늘
Beep(freq(1,'미'),int(1*t)-d) #도
Beep(freq(1,'파샾'),int(0.5*t)-d) #그
Beep(freq(1,'미'),int(0.25*t)-d) #대
Beep(freq(1,'도샾'),int(0.75*t)-d) #만
Beep(freq(1,'도샾'),int(0.5*t)-d) #생
Beep(freq(1,'레'),int(0.5*t)-d) #각
Beep(freq(1,'레'),int(0.5*t)-d) #해
Beep(freq(1,'레'),int(1*t)-d) #암
Beep(freq(1,'레샾'),int(0.5*t)-d) #욜
Beep(freq(1,'레샾'),int(1*t)-d) #맨
Beep(freq(0,'라샾'),int(0.5*t)-d) #암
Beep(freq(0,'라샾'),int(0.5*t)-d) #욜
Beep(freq(1,'레샾'),int(0.5*t)-d) #맨
Beep(freq(1,'레샾'),int(0.5*t)-d) #그
Beep(freq(1,'파샾'),int(0.25*t)-d) #대
Beep(freq(1,'레샾'),int(0.75*t)-d) #여
time.sleep((t*0.75-d)/1000) # 쉬고
Beep(freq(0,'라샾'),int(0.25*t)-d) #다
Beep(freq(0,'라샾'),int(0.25*t)-d) #라
Beep(freq(0,'라샾'),int(0.25*t)-d) #다
Beep(freq(1,'레샾'),int(0.25*t)-d) #따
Beep(freq(1,'레샾'),int(0.5*t)-d) #오
Beep(freq(1,'도샾'),int(0.5*t)-d) #늘
Beep(freq(1,'레샾'),int(1*t)-d) #도
time.sleep((t*0.75-d)/1000) # 쉬고
Beep(freq(1,'레샾'),int(0.25*t)-d) #그
Beep(freq(1,'레샾'),int(0.25*t)-d) #대
Beep(freq(1,'레샾'),int(0.5*t)-d) #가
Beep(freq(1,'레샾'),int(0.5*t)-d) #떠
Beep(freq(1,'레샾'),int(0.5*t)-d) #나
Beep(freq(1,'레샾'),int(0.25*t)-d) #지
Beep(freq(1,'파'),int(0.5*t)-d) #않
Beep(freq(1,'파'),int(0.5*t)-d) #아
time.sleep((t*1-d)/1000) # 쉬고
Beep(freq(1,'레'),int(0.75*t)-d) #암
Beep(freq(1,'파'),int(0.75*t)-d) #욜
Beep(freq(1,'레샾'),int(0.5*t)-d) #맨
time.sleep((t*0.5-d)/1000) # 쉬고
