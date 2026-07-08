# Momentum tilt: three mechanisms, zero value added

Across deadband, CPI sign correction, and sticky-flat hysteresis, the momentum tilt adds nothing. Every apparent improvement traces back to exposure — being in the market longer or more fully — not to any actual timing skill. Verdict first, evidence below.

## 1. Deadband (Day 17)

**Decision:** widen the symmetric band to cut whipsaw.

**Killed:** it doesn't work. Baseline turnover at band = 1.0 was 15 transitions in the calm window (2016–2018), 7 in the shock window (2020–2022), 41 over the whole series — and widening the band doesn't bring those down. The reason is mechanical: the flat state isn't sticky, so every noise flip becomes an *enter-and-exit pair* (accel → flat → decel) rather than being absorbed. On top of that, the slow 3-month MA + 3-month delta transform loiters near zero in calm periods, which is exactly where the whipsaw lives. Whipsaw isn't a threshold problem, it's a lag/mechanism problem, and no amount of band-widening fixes a signal that's structurally late. This diagnosis — *the flat state is non-sticky* — is what pointed directly at the Day 19 fix below.

## 2. CPI sign-table (Day 18)

**Decision:** flip one cell so accelerating inflation de-risks instead of leaning in. Tested honestly against a leakage-free, z-scored baseline.

**Killed:** net −0.064x, worse than doing nothing. The mechanism failure is specific — a single momentum signal can't distinguish a 2021 rally from a 2022 selloff when both show the same acceleration reading. Because 2022 classifies as an Inflationary Boom (not Stagflation), the flipped cell fires in *both* years: de-risking into the 2021 recovery rally (costly) and the 2022 selloff (beneficial) — and the rally cost outweighs the selloff benefit. Fixing the label doesn't fix the underlying blindness; the missing ingredient is growth momentum underneath the inflation reading, not the CPI state.

## 3. Sticky-flat hysteresis (Day 19)

**Decision:** asymmetric hold — enter at ±1.5, only exit on a far-threshold crossing — to cut noisy transitions. This is the direct fix for the non-sticky flat state diagnosed on Day 17.

**Killed by a state-occupancy check.** On the equity curve it looked like the first real win: 2.07 → 2.22. But sticky spends 0 months flat versus symmetric's 97. It's fully tilted for two-thirds of the period symmetric would have sat neutral, and transitions drop to 4 (from 26) — it's barely reacting to the signal at all. The 2.22 is uncompensated equity exposure across a bull market, not timing skill: the mechanism picks a direction and sits in it for ~37 months at a stretch, and "hold an equity overweight through the 2010s–2020s" is a known winning bet that has nothing to do with the regime signal being smart.

**Caveat:** there's a small, real second-order effect — the hold kept it de-risked through the 2022 drawdown instead of flip-flopping out — but it's nowhere near enough to carry the mechanism, and it rides on the same "barely reacts" property that makes the tilt useless the rest of the time.

## Through-line

Across every variant, the outperformance was exposure wearing a timing costume, and the state-occupancy check was the tool that told the difference. The honest negative result — three independent mechanisms, three failures, same root cause — is the finding.