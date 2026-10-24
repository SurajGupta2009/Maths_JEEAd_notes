---
id: jee-01
part: jee
title: "Rates of Change and Related Rates"
---

## Differentiate the relation with respect to time

If $y=f(x)$ and $x$ changes with time $t$, the chain rule gives
$$
\frac{dy}{dt}=f'(x)\frac{dx}{dt}.
$$
The average rate over a time interval is a secant slope; the instantaneous rate is its limit. Units provide a check: if $r$ is in cm and $t$ in seconds, then $d(\pi r^2)/dt$ is in cm$^2$/s.

:::example title="Circle, cube and balloon: choose the geometric relation first"
For a circle with $dr/dt=2$ cm/s,
$$
A=\pi r^2,\qquad \frac{dA}{dt}=2\pi r\frac{dr}{dt}=4\pi r.
$$
At $r=5$, the area grows at $20\pi$ cm$^2$/s.

For a cube with $ds/dt=3$ cm/min,
$$
V=s^3,\qquad \frac{dV}{dt}=3s^2\frac{ds}{dt},
$$
so $s=10$ gives $900$ cm$^3$/min.

For a spherical balloon with $dV/dt=100$ cm$^3$/s,
$$
V=\frac{4}{3}\pi r^3,\qquad \frac{dV}{dt}=4\pi r^2\frac{dr}{dt}.
$$
Thus at $r=10$, $dr/dt=1/(4\pi)$ cm/s, approximately $0.0796$ cm/s.
:::

:::example title="The 13 m ladder: a negative rate means descent"
Let $x$ be the foot's distance from the wall and $y$ the top's height. Then
$$
x^2+y^2=169
\quad\Longrightarrow\quad
2x\frac{dx}{dt}+2y\frac{dy}{dt}=0.
$$
When $x=5$, $y=12$ and $dx/dt=1/2$, so
$$
\frac{dy}{dt}=-\frac{x}{y}\frac{dx}{dt}
=-\frac{5}{12}\cdot\frac{1}{2}=-\frac{5}{24}\text{ m/s}.
$$
The top descends at $5/24$ m/s, approximately $0.2083$ m/s.
:::

:::diagram
{
  "type": "flow",
  "title": "A related-rates calculation keeps every variable alive",
  "steps": [
    {"title": "Draw and name", "detail": "Assign variables, signs and units to each changing quantity."},
    {"title": "Write the relation", "detail": "Use area, volume, Pythagoras or another geometric constraint."},
    {"title": "Differentiate in time", "detail": "Apply the chain rule before inserting instantaneous values."},
    {"title": "Substitute and solve", "detail": "Insert rates and coordinates, then interpret the sign."}
  ],
  "caption": "Substituting a length before differentiating would freeze that length and incorrectly make its rate zero."
}
:::

:::warn title="Differentiate first, substitute last"
A numerical value such as $x=5$ describes one instant. It does not say that $x$ is constant while the ladder moves. Keep $x$ and $y$ variable until after the time derivative has been formed.
:::
