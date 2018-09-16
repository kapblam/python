import matplotlib.pyplot as plt
import numpy as np
import wave
import struct

# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.figure(2)
# plt.plot([1,2,3,4],[1,4,9,16], 'ro')
# plt.axis([0,6,0,20])
#
# t = np.arange(0,5,0.2)
# plt.figure()
# plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
#
# plt.figure()
# data = {'a':np.arange(50),
#         'c':np.random.randint(0,50,50),
#         'd':np.random.randn(50)}
# data['b'] = data['a'] + 10*np.random.randn(50)
# data['d'] = np.abs(data['d'])*100
#
# plt.scatter('a','b',c='c',s='d',data=data)
#
# plt.figure()
#
# x = np.linspace(0,2*np.pi,201)
# y = np.sin(2*np.pi*3*x)
# plt.plot(x,y)
#
# plt.figure()
# yh = np.fft.fft(y)
# plt.plot(np.fft.fftfreq(y.size),yh)
# plt.show()

if __name__=='__main__':
    #make wav file
    freq = 261.626
    freq2 = 329.628
    freq3 = 391.995
    data_size = 40000
    fname = "test.wav"
    frate = 11025.0
    amp = 64000.0
    nchannels = 1
    sampwidth = 2
    framerate = int(frate)
    nframes = data_size
    comptype = "NONE"
    compname = "not compressed"
    def c(x):
        return np.sin(2*np.pi*freq*(x/frate))
    def e(x):
        return np.sin(2*np.pi*freq2*(x/frate))
    def g(x):
        return np.sin(2*np.pi*freq3*(x/frate))
    data = [c(x) for x in range(data_size)]
    data2 = [e(x) for x in range(data_size)]
    data3 = [g(x) for x in range(data_size)]
    result2 = np.divide(np.add(data,data2),2)
    result = np.divide(np.add(np.add(data,data2),data3),3)

    wav_file = wave.open(fname,'w')
    wav_file.setparams((nchannels,sampwidth,framerate,nframes,comptype,compname))

    count = 0
    rec = np.zeros(len(result))
    while 1:
        if count < int(data_size/3):
            rec[count] = data[count]
            count = count +1
        elif count < int(data_size/3)*2:
            rec[count] = result2[count]
            count = count +1
        elif count < int(data_size/3)*3+1:
            rec[count] = result[count]
            count = count+1
        else:
            break
    for v in rec:
        wav_file.writeframes(struct.pack('h',int(v*amp/2)))
        # wav_file.writeframes(struct.pack('h',int(v*amp/2)))
    wav_file.close()
    print(len(rec))

    plt.subplot(2,3,1)
    plt.plot(np.arange(data_size),data)
    plt.title("C4")
    plt.axis([0,500,-1,1])

    plt.subplot(2,3,2)
    plt.plot(np.arange(data_size),data2)
    plt.title("E4")
    plt.axis([0,500,-1,1])

    plt.subplot(2,3,3)
    plt.plot(np.arange(data_size),data3)
    plt.title("G4")
    plt.axis([0,500,-1,1])

    plt.subplot(2,3,4)
    plt.plot(np.arange(data_size),result2)
    plt.title("C4+E4")
    plt.axis([0,500,-1,1])
    plt.subplot(2,3,5)
    plt.plot(np.arange(data_size),result)
    plt.title("C4+E4+G4")
    plt.axis([0,500,-1,1])
    plt.subplot(2,3,6)
    plt.plot(np.arange(data_size),rec)
    plt.title("rec")
    plt.axis([0,500,-1,1])

    # plt.show()

    #read/process wav_file
    wav_file = wave.open(fname,'r')
    data = wav_file.readframes(data_size)
    wav_file.close()
    data = struct.unpack('{n}h'.format(n=data_size),data)
    data = np.array(data)

    w = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(w))
    print(freqs.min(), freqs.max())

    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freqHz = np.abs(freq*frate)
    print(freq)
    print(freqHz)

    test = np.max(np.abs(w))
    print(test)
    tstm = np.zeros(len(w))
    for r in np.abs(w):
        if r > test*0.1:
            tstm[np.where(np.abs(w)==r)] = r
    flag = 1
    flag1 = 0
    flag2 = 0
    start1=0
    start2=0
    start3 = 0
    tstm = tstm[0:20000]
    for y in tstm:
        if y>0 and flag:
            start1 = np.where(tstm==y)[0][0]
            flag = 0
            flag1 = 1
        elif y>0 and flag1:
            start1 = np.append(start1,np.where(tstm==y)[0][0])
        # else:
        #     flag = 0
        #     flag1 = 1
        #
        # if y>0 and flag1:
        #     start2 = np.where(tstm==y)[0][0]
        #     flag1 = 0
        # if y>0 and flag2:
        #     start3 = np.where(tstm==y)[0][0]
        #     flag2 = 0
    plt.figure()
    plt.plot(freqs,np.abs(w))
    print(start1)
    print(freqs[start1]*frate,freqs[start2]*frate,freqs[start3]*frate)

    plt.show()
