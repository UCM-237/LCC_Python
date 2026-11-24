"""Genera las figuras nuevas del capítulo 9 (integracion.tex) (revisión 2026).
Uso, desde la raíz del repositorio:  python tools/figuras/figuras_cap9.py
"""
import os
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
import sys, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0,os.path.join(RAIZ,'codigos','diferenciacion_integracion'))
from Euler_method import euler
from amortiguador_test import amortiguador
plt.rcParams.update({'font.size':11})
F=os.path.join(RAIZ,'figuras','')
# 1 error vs h
h=np.logspace(-15,0,61); x0=1.0
ef=abs((np.sin(x0+h)-np.sin(x0))/h-np.cos(x0)); ec=abs((np.sin(x0+h)-np.sin(x0-h))/(2*h)-np.cos(x0))
fig,ax=plt.subplots(figsize=(7,4.2))
ax.loglog(h,ef,'o-',ms=4,label='adelantada / forward')
ax.loglog(h,ec,'s-',ms=4,label='centrada / central')
hh=np.logspace(-7,-1,10); ax.loglog(hh,20*0.5*np.sin(x0)*hh,color='gray',ls='--',lw=0.8); ax.text(1e-4,3e-2*0.84*10*1e-4/1e-4*1e-1,'$\\propto h$',color='gray')
hh=np.logspace(-4,-1,10); ax.loglog(hh,20*np.cos(x0)/6*hh**2,color='gray',ls=':',lw=1); ax.text(3e-3,1e-5,'$\\propto h^2$',color='gray')
hh=np.logspace(-15,-9,10); ax.loglog(hh,20*2.2e-16/hh,color='gray',ls='-.',lw=0.8); ax.text(1e-12,3e-2,'$\\propto 1/h$',color='gray')
ax.set_xlabel('$h$'); ax.set_ylabel('error'); ax.legend(loc='lower left')
ax.set_ylim(1e-14,10)
fig.tight_layout(); fig.savefig(F+'errores_derivada.pdf')
# 2 damper
fig,axs=plt.subplots(3,1,figsize=(7,7.5),sharex=True)
for ax,(k,hs) in zip(axs,[(10.,0.01),(100.,0.01),(100.,0.001)]):
    t,y=euler(lambda t,y: amortiguador(t,y,k=k),[0,0],0,50,hs)
    ax.plot(t,y[0],lw=0.8)
    ax.axhline(2*9.8/k,color='k',ls='--',lw=0.7)
    ax.set_ylabel('$y$ (m)'); ax.set_title(f'$k={k:g}$ N/m, $h={hs:g}$ s',fontsize=11)
axs[-1].set_xlabel('$t$ (s)')
fig.tight_layout(); fig.savefig(F+'amortiguador_euler.pdf')
# 3 RC
def condensador(t,Vo,C=1.,R=1.,Vi=10.): return (Vi-Vo)/(R*C)
fig,ax=plt.subplots(figsize=(7,4.2))
tt=np.linspace(0,10,400); ax.plot(tt,10*(1-np.exp(-tt)),'k',lw=1,label='$10(1-e^{-t})$')
for hs,m in [(0.5,'o'),(0.25,'s')]:
    t,V=euler(condensador,0,0,10,hs); ax.plot(t,V[0],m+'--',ms=4,lw=0.8,label=f'Euler, $h={hs}$ s')
ax.set_xlabel('$t$ (s)'); ax.set_ylabel('$V_o$ (V)'); ax.legend(loc='lower right'); ax.set_xlim(0,6)
fig.tight_layout(); fig.savefig(F+'solrc.pdf')
print('ok', ef.min(), h[ef.argmin()], ec.min(), h[ec.argmin()])
