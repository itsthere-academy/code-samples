#%%
import spiceypy as spice
import numpy as np
import plotly.graph_objects as go


METAKR = 'getsta.tm'

spice.tkvrsn('TOOLKIT')
spice.unload(METAKR)
spice.furnsh(METAKR)


def gen_pos(object, observer, ref, start, end, delta):
    pos = []

    t = start
    while t < end:
        (pos_t, _) = spice.spkpos(object, t, ref, 'NONE', observer)
        pos.append(pos_t)

        t += delta

    return np.array(pos)


#%%
t_start = spice.str2et('2021-01-01T00:00:00')
t_delta = spice.str2et('2021-01-01T04:00:00') - t_start
t_end = spice.str2et('2022-01-01T00:00:00')

earth = gen_pos('EARTH', 'SOLAR SYSTEM BARYCENTER', 'ECLIPJ2000', t_start, t_end, t_delta)
moon = gen_pos('MOON', 'SOLAR SYSTEM BARYCENTER', 'ECLIPJ2000', t_start, t_end, t_delta)

#%%
fig = go.Figure()

fig.add_trace(
    go.Scatter3d(
        x = earth[:, 0],
        y = earth[:, 1],
        z = earth[:, 2],
        mode='lines',
        name='Earth'
    )

)

fig.add_trace(
    go.Scatter3d(
        x = moon[:, 0],
        y = moon[:, 1],
        z = moon[:, 2],
        mode='lines',
        name='Moon'
    )
)

fig.show()
