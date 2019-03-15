import tkinter
from datetime import datetime,timedelta


window=tkinter.Tk()
window.title('打卡计时')
window.resizable(0,0)
width=500
height=320

screenwidth=window.winfo_screenwidth()
screenheight=window.winfo_screenheight()
alignstr= '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
window.geometry(alignstr)


#获取当前时间
def get_datetime():
    t1=datetime.now()
    t = datetime.strftime(t1, '%Y-%m-%d-%w %H:%M:%S')
    y = t[:4]
   # print("年：", y)
    m = t[5:7]
    #print('月：', m)
    d = t[8:10]
    #print('日：', d)
    weekday = {
        1: "星期一",
        2: '星期二',
        3: '星期三',
        4: '星期四',
        5: '星期五',
        6: '星期六',
        7: '星期日'
    }
    w = weekday.get(t1.isoweekday())
    #print("周：", w)
    time = t[-8:]
    #print(time)
    return {
        '年':y,
        '月':m,
        '日':d,
        '周':w,
        '时间':time
    }

def show_datetime():
    global var_showdatetime_label
    datetime_dict=get_datetime()
    datetime_show=datetime_dict.get('年')+'年'+datetime_dict.get('月')+'月'+datetime_dict.get('日')+'日'+' '+datetime_dict.get('周')+'\n'+datetime_dict.get('时间')
    var_showdatetime_label.set(datetime_show)
    data_label.after(500,show_datetime)

var_uptime_entry=tkinter.Variable()
var_uptime_entry.set('')

var_showdatetime_label=tkinter.Variable()
var_showdatetime_label.set('')

var_predict_offtime_label=tkinter.Variable()
var_predict_offtime_label.set('')

var_actual_offtime_label=tkinter.Variable()
var_actual_offtime_label.set('')

data = datetime.strftime(datetime.now(), '%Y-%m-%d')

uptime=None
predict_off_time=None
actual_offtime=None
text1=''
text=''
#text = '%s:\n     上班时间  ：%s\n   预计下班时间：%s\n   实际下班时间：18:11\n' % (data,uptime,off_time)


def click_uptime():#点击打卡按钮
    global var_uptime_entry,var_predict_offtime_label,var_actual_offtime_label
    global uptime,predict_off_time
   # var_uptime_entry.set('{}'.format(time.ctime()))
    updatetime=get_datetime()
    uptime=updatetime.get('时间')
    var_uptime_entry.set(uptime)#点击打卡时，显示当前打卡时间
    click_button.config(state=tkinter.DISABLED)#点击打卡后将打卡按钮设置不可用，当点下班按钮后重新激活

    d=datetime.strptime(uptime,'%H:%M:%S')
    off_time=datetime.strftime((d+timedelta(hours=9.5)),'%H:%M:%S')
    #print(off_time)
    var_predict_offtime_label.set(off_time)

    predict_off_time=off_time
    var_actual_offtime_label.set('')
   # return 1

def click_off():#点击下班按钮
    global var_actual_offtime_label
    global text1,text,actual_offtime
    off_time=get_datetime().get('时间')
    var_actual_offtime_label.set(off_time)

    click_button.config(state=tkinter.NORMAL)#重新将打卡按钮激活

    actual_offtime=off_time
    text = '%s:\n     上班时间  ：%s\n   预计下班时间：%s\n   实际下班时间：%s\n' % (data, uptime, predict_off_time,actual_offtime)

  #  if click_button.cget('state') == 'disabled':
    text1 =text1+ text





def click_history():#点击历史按钮
    #global history_flag
    global text,text1,predict_off_time
    history_window = tkinter.Toplevel(window)

  #  if not history_flag:
       # history_window=tkinter.Toplevel(window)
        # history_window.geometry('300x320')
    history_window.title('历史记录')
    window_x=window.winfo_x()+500
    window_y=window.winfo_y()
    history_window.geometry('300x320+%d+%d'%(window_x,window_y))
    history_window.resizable(0,0)

    text_scroll=tkinter.Scrollbar(
        history_window
    )
    text_scroll.pack(side=tkinter.RIGHT,fill='y')

    history_text=tkinter.Text(
        history_window,
        bg='red',
       # height=20,
        yscrollcommand=text_scroll.set
    )
    text_scroll.config(command=history_text.yview)
    history_text.pack(side=tkinter.TOP)

 #   data = datetime.strftime(datetime.now(), '%Y-%m-%d')
    # uptime=''
    # predict_offtime=''
    # actual_offtime=''
 #   text='%s:\n     上班时间  ：08:41\n   预计下班时间：18:11\n   实际下班时间：18:11\n'%data

 #   print('text1=',text1,'text=',text)
    if not uptime ==None:
        history_text.insert(tkinter.INSERT, text1)
        history_text.config(state=tkinter.DISABLED)
   # print(uptime,predict_off_time)
 #   text+=text
 #   print(click_button.cget('state'))
   # if click_button.cget('state')=='disabled':
    #        text+=text

    #打开历史窗口后把“历史按钮设置不可用”
    history_button.config(state=tkinter.DISABLED)
    def closs():
        history_window.destroy()
        history_button.config(state=tkinter.NORMAL)
    #监听历史窗口关闭事件，点击关闭时，调用closs关闭历史窗口，并且重新开放“历史”按钮
    history_window.protocol("WM_DELETE_WINDOW",closs)
       # history_flag=True

     #  def callback():pass
      #  history_window.protocol("WM_DELETE_WINDOW",callback)
       # history_window.mainloop()

   # else:
      #  print('guanbi')
       # history_window.destroy()

        # print(type(window_x))
        # print('x:'+str(window.winfo_x()))
        # print('y:'+str(window.winfo_y()))

#fm1
fm1=tkinter.Frame(window,width=320)
data_label=tkinter.Label(       #显示日期的label
    fm1,
#    text='2019年3月8日 星期五\n'+'23:09',
    bg='green',
    width=20,height=1,
    textvariable=var_showdatetime_label
)
data_label.pack(side=tkinter.LEFT,anchor=tkinter.W,ipady=20,ipadx=7)


history_button=tkinter.Button(              #历史按钮
    fm1,
    text='历史',
    bg='red',
    command=click_history
)
#history_button.grid(row=0,column=5,sticky=tkinter.E,rowspan=1,ipadx=10,ipady=7,padx=320)
history_button.pack(side=tkinter.RIGHT,anchor='ne',ipadx=5,ipady=3)

fm1.pack(side=tkinter.TOP,fill='x')
#fm1.grid(row=0,column=0,columnspan=2,sticky=tkinter.E+tkinter.W+tkinter.S+tkinter.N)

#fm2
fm2=tkinter.Frame(window)

click_button=tkinter.Button(                #打卡按钮
    fm2,
    text='上班',
    bg='red',
    width=8,
    height=2,
    command=click_uptime
)
#click_button.grid(row=1,column=1,columnspan=2,ipadx=30,ipady=10,padx=10,pady=10)
click_button.place(relx=0.25,rely=0.5,anchor='w')

off_button=tkinter.Button(                  #下班按钮
    fm2,
    text='下班',
    bg='red',
    width=8,
    height=2,
    command=click_off
)
off_button.pack(side=tkinter.RIGHT,padx=120)

fm2.pack(side=tkinter.TOP,fill='x',pady=25)
#fm2.grid(row=1,column=0,columnspan=2,sticky=tkinter.E+tkinter.W+tkinter.S+tkinter.N)

#fm3
fm3=tkinter.Frame(window,width=100)

uptime_label=tkinter.Label(      #显示‘打卡时间’的label
    fm3,
    text='上班时间',
    bg='red'

)
uptime_label.pack(expand=tkinter.YES,fill='x')

predict_offtime_label=tkinter.Label(      #显示“预计下班时间”的label
    fm3,
    text='预计下班时间',
    bg='red'
)
predict_offtime_label.pack(expand=tkinter.YES,fill='x',pady=5)

actual_offtime_label=tkinter.Label(        #显示“实际下班时间”的label
    fm3,
    text='实际下班时间',
    bg='red'
)
actual_offtime_label.pack(expand=tkinter.YES,fill='x')

fm3.pack(side=tkinter.LEFT,fill='y',pady=15,expand=tkinter.YES)
#fm3.grid(row=2,column=0)


#fm4
fm4=tkinter.Frame(window)

uptime_entry=tkinter.Entry(                 #显示打卡时间的输入框
    fm4,
    bg='red',
    state='readonly',
    width=40,
    font=("Arial", 12),
    fg='red',
    justify=tkinter.CENTER,
    textvariable=var_uptime_entry


)
uptime_entry.pack(expand=tkinter.YES,fill='x',padx=10)

predict_offtime_entry=tkinter.Entry(        #显示预计下班时间的输入框
    fm4,
    bg='red',
    state='readonly',
    width=40,
    font=("Arial", 12),
    fg='red',
    justify=tkinter.CENTER,
    textvariable=var_predict_offtime_label
)
predict_offtime_entry.pack(expand=tkinter.YES,fill='x',padx=10,pady=5)

actual_offtime_entry=tkinter.Entry(          #显示实际下班时间的输入框
    fm4,
    bg='red',
    state='readonly',
    width=40,
    font=("Arial", 12),
    fg='red',
    justify=tkinter.CENTER,
    textvariable=var_actual_offtime_label
)
actual_offtime_entry.pack(expand=tkinter.YES,fill='x',padx=10)


fm4.pack(side=tkinter.LEFT,anchor='nw',fill='both',pady=15,expand=tkinter.YES)
#fm4.grid(row=2,column=1)





data_label.after(500,show_datetime)



window.mainloop()