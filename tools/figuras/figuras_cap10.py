"""Genera las figuras nuevas del capítulo 10 (tratamientoest.tex) (revisión 2026).
Uso, desde la raíz del repositorio:  python tools/figuras/figuras_cap10.py
"""
import os
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.stats import norm, t as tdist
plt.rcParams.update({'font.size': 11})
F = os.path.join(RAIZ, 'figuras', '')

# 1 dado trucado / biased die
v = np.arange(1, 7); p = np.array([.1]*5 + [.5]); P = np.cumsum(p)
fig, ax = plt.subplots(figsize=(7, 4.2))
ax.stem(v - 0.06, p, linefmt='C3-', markerfmt='C3o', basefmt=' ',
        label='distribución / distribution $P(n)$')
ax.stem(v + 0.06, P, linefmt='C0-', markerfmt='C0s', basefmt=' ',
        label='acumulada / cumulative $P(n\\leq x)$')
ax.set_yticks([0, .1, .2, .3, .4, .5, 1])
ax.set_yticklabels(['0', '1/10', '2/10', '3/10', '4/10', '1/2', '1'])
ax.grid(axis='y', ls=':')
ax.set_xlabel('valor del dado / die value'); ax.set_ylabel('probabilidad / probability')
ax.legend(loc='upper left'); ax.set_ylim(0, 1.08)
fig.tight_layout(); fig.savefig(F + 'dadot.pdf')

# 2 exponencial / exponential (mu = 1)
x = np.linspace(0, 8, 400); mu = 1.0
fig, ax = plt.subplots(figsize=(7, 4.2))
ax.plot(x, np.exp(-x/mu)/mu, label='$f(x)=e^{-x/\\mu}/\\mu$, $\\mu=1$')
ax.plot(x, 1 - np.exp(-x/mu), label='acumulada / cumulative $F(x)$')
xs = np.linspace(1, 2, 50); ax.fill_between(xs, np.exp(-xs), color='C0', alpha=0.4)
pr = np.exp(-1) - np.exp(-2)
ax.annotate('$P(1\\leq x\\leq 2)=e^{-1}-e^{-2}=%.3f$' % pr, xy=(1.5, 0.15),
            xytext=(2.8, 0.55), arrowprops=dict(arrowstyle='->'))
ax.set_xlabel('$x$'); ax.set_ylabel('probabilidad / probability')
ax.legend(loc='lower right'); ax.set_ylim(0, 1.05)
fig.tight_layout(); fig.savefig(F + 'distexp.pdf')

# 3 teorema central del límite (mismo cálculo que central_limit.py)
gen = np.random.default_rng(1000); N = 100_000
xx = np.linspace(-0.9, 0.9, 400)
fig, axs = plt.subplots(1, 2, figsize=(8, 3.6))
for ax, n in zip(axs, [10, 100]):
    med = (2*gen.random((N, n)) - 1).mean(axis=1); s2 = (4/12)/n
    ax.hist(med, bins=50, density=True)
    ax.plot(xx, np.exp(-xx**2/(2*s2))/np.sqrt(2*np.pi*s2), 'C1')
    ax.set_xlabel('$\\bar{x}_{%d}$' % n); ax.set_xlim(-0.9, 0.9)
axs[0].set_ylabel('densidad / density')
fig.tight_layout(); fig.savefig(F + 'tlc.pdf')

# 4 RANDU
I = np.empty(30001, dtype=np.int64); I[0] = 1
for k in range(1, len(I)):
    I[k] = (65539*I[k-1]) % 2**31
u = I/2**31
w = np.random.default_rng(1).random(30001)
fig = plt.figure(figsize=(8, 3.8))
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.scatter(u[:-2:3][:3000], u[1:-1:3][:3000], u[2::3][:3000], s=1, c='C3')
ax.set_proj_type('ortho')
# dirección de visión contenida en los planos 9x-6y+z=cte
E=np.radians(8); A=np.arctan2(6,9); A=-A+np.arccos(-np.sin(E)/np.sqrt(117)/np.cos(E))
ax.view_init(elev=8, azim=np.degrees(A))
ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
ax.set_box_aspect(None, zoom=1.35)
ax.set_title('RANDU $(u_k,u_{k+1},u_{k+2})$', fontsize=10)
ax2 = fig.add_subplot(1, 2, 2)
ax2.hist(9*w[:-2] - 6*w[1:-1] + w[2:], bins=300, color='C0', alpha=0.6,
         label='PCG64 (numpy)')
ax2.hist(9*u[:-2] - 6*u[1:-1] + u[2:], bins=300, color='C3',
         label='RANDU')
ax2.set_xlabel('$9u_k-6u_{k+1}+u_{k+2}$'); ax2.legend(loc='upper left', fontsize=9)
ax2.set_yticks([])
fig.tight_layout(); fig.savefig(F + 'randu.pdf')

# 5 cobertura de 100 intervalos del 95 % / coverage
rng = np.random.default_rng(7); n = 5; mu, sig = 20.0, 0.5
x = rng.normal(mu, sig, (100, n)); m = x.mean(1); se = x.std(1, ddof=1)/np.sqrt(n)
fig, axs = plt.subplots(1, 2, figsize=(8, 4.6), sharey=True)
for ax, (k, nom) in zip(axs, [(norm.ppf(0.975), 'normal'),
                              (tdist.ppf(0.975, n-1), 't de Student / Student t')]):
    fuera = np.abs(m - mu) > k*se
    for i in range(100):
        ax.plot([m[i]-k*se[i], m[i]+k*se[i]], [i, i],
                color='C3' if fuera[i] else 'C0', lw=1.5 if fuera[i] else 0.8)
    ax.axvline(mu, color='k', ls='--', lw=0.8)
    ax.set_title('%s: %d de 100 fallan' % (nom, fuera.sum()), fontsize=10)
    ax.set_xlabel('$\\bar{x}\\pm k\\,s/\\sqrt{n}$')
    print(nom, fuera.sum())
axs[0].set_ylabel('experimento / experiment')
fig.tight_layout(); fig.savefig(F + 'cobertura.pdf')

# 6 propagación por Monte Carlo / Monte Carlo propagation
T = np.array([55.7, 62.8, 58.1, 60.9, 66.3, 59.4, 61.8, 62.5, 59.4, 61.4,
              55.7, 65.3, 56.9, 57.8, 62.9, 59.9, 62.6, 59.1, 57.9, 53.8])
V = np.array([761, 897, 879, 767, 758, 763, 762, 761, 790, 852,
              816, 752, 848, 920, 743, 858, 761, 788, 775, 791])*1e-3
b = 0.004; rng = np.random.default_rng(2026); N = 1_000_000
Ps = (rng.normal(V.mean(), V.std(ddof=1)/np.sqrt(20), N)**2 /
      (rng.normal(100, 5/norm.ppf(0.99), N) *
       (1 + b*(rng.normal(T.mean(), T.std(ddof=1)/np.sqrt(20), N)
               - rng.uniform(49.9, 50.1, N)))))*1e3
P0 = V.mean()**2/(100*(1 + b*(T.mean() - 50)))*1e3; uP = 0.2294
fig, ax = plt.subplots(figsize=(7, 4.2))
ax.hist(Ps, bins=200, density=True, alpha=0.6, label='Monte Carlo ($10^6$)')
pp = np.linspace(5.1, 7.3, 400)
ax.plot(pp, norm.pdf(pp, P0, uP), 'k', label='lineal / linear: $N(P,u_c^2)$')
ax.set_xlabel('$P$ (mW)'); ax.set_ylabel('densidad / density'); ax.legend()
fig.tight_layout(); fig.savefig(F + 'propagacion_mc.pdf')
print('MC', Ps.mean(), Ps.std(), np.percentile(Ps, [2.5, 97.5]))
