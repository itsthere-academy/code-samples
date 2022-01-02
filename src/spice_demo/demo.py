# Copyright 2022 Piotr Szukalski

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#%%
import spiceypy as spice
import numpy as np
import plotly.graph_objects as go


METAKR = 'getsta.tm'

spice.tkvrsn('TOOLKIT')
spice.unload(METAKR)

# The crucial bit - load the kernels (data files)
spice.furnsh(METAKR)


def gen_pos(object, observer, ref, start, end, delta):
    """
    Generate x, y, z coordinates (ephemerids) for given time frame.

    :param object: the body to generate the ephemerids for
    :param observer: object observing the movement, or relative to what body the object moves?
    :param ref: reference frame, or coordinates system (e.g. "ECLIPJ2000" for the ecliptic)
    :param start: initial timestamp in TBD (Barycentric Dynamical Time)
    :param end: final timestamp in TBD
    :param delta: time increment (resolution)

    :return: ndarray of (x, y, z) coodrindates - ndarray shape is [n, 3], where n is floor((end - start)/delta)
    """
    pos = []

    t = start
    while t < end:
        # spkpos returns two vectors - position and velocity. We care the position only for now.
        (pos_t, _) = spice.spkpos(object, t, ref, 'NONE', observer)
        pos.append(pos_t)

        t += delta

    return np.array(pos)


#%%
# Bespoke way to tell - we want data for the whole 2021 with 4h intervals
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

#%%
# and this is how you can save the graph to a file
# fig.write_html("/tmp/graph.html", include_plotlyjs='cdn', include_mathjax='cdn', full_html=False)