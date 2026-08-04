---
layout: post
title: "Probability → Data Science"
chapter: '03'
order: 4
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
lesson_type: required
---

A model that scores 99% accuracy on a training set can still fail in production. A poll of a thousand people can predict an election—or embarrass its authors. A spam filter that never errs on yesterday’s mail can miss tomorrow’s campaign. **Probability** is the language that turns those failures into objects you can define, measure, and sometimes bound.

**Path:** randomness as modeling → expectation and variance → LLN and CLT → inference → risk in machine learning → causality caution → confusions.

This lecture is not a full probability course. It is a map of **why probability became the operating system of data science**: sampling, uncertainty, and learning from incomplete information.

---

## Learning objectives

After this lecture you should be able to:

- Distinguish data as fixed numbers from data as realizations of random variables (the modeling move).
- State the **law of large numbers (LLN)** and **central limit theorem (CLT)** at slogan-and-formula level and say what they justify in practice.
- Explain estimation, confidence, and hypothesis testing as *inferences under uncertainty*, not as magical truth certificates.
- Define **risk** as expected loss and connect empirical risk minimization to “training loss.”
- Name why correlation is not causation and why deployment shift breaks naive validation.
- Avoid “probability is only gambling” and “big data eliminates uncertainty.”

**Prerequisites.** Averages, basic counting. Helpful: integrals for continuous densities; the [linear algebra]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/) view of data matrices.

**Seminar links.** LO-style data literacy; pairs with [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), [Math of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/).

---

## 1. The modeling move: data as random

In pure computation, an array of numbers is just an array. In data science, we often treat observations $$X_1,\ldots,X_n$$ as **random variables**—quantities that could have been otherwise under a hypothetical repeat of the world (or a draw from a population / data-generating process).

A **probability distribution** assigns weights (or densities) to possible outcomes. Discrete example: Bernoulli($$p$$) for a coin with $$P(X=1)=p$$. Continuous example: a normal density

$$
f(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\Bigl(-\frac{(x-\mu)^2}{2\sigma^2}\Bigr).
$$

**Why model at all?** Because we want statements that travel beyond the spreadsheet: predictions for new customers, error bars for a mean, guarantees that a learning algorithm’s average performance concentrates.

**Mechanism slogan.**  
*Probability turns “what happened” into “what process could have produced what happened—and what will happen next.”*

---

## 2. Expectation, variance, and the algebra of averages

The **expectation** $$\mathbb{E}[X]$$ is the probability-weighted average of $$X$$—the center of mass of the distribution. For a function $$g$$, $$\mathbb{E}[g(X)]$$ is what long-run averages of $$g(X_i)$$ approach under LLN conditions.

**Variance** $$\mathrm{Var}(X)=\mathbb{E}[(X-\mathbb{E}X)^2]$$ measures spread. Linearity of expectation

$$
\mathbb{E}[aX+bY]=a\mathbb{E}[X]+b\mathbb{E}[Y]
$$

holds even when $$X$$ and $$Y$$ are dependent—an underrated workhorse of randomized algorithms and sampling proofs. Variance is less friendly: variances add for *independent* (or uncorrelated) sums, which is why independent averaging reduces noise.

In data science:

- Metrics (CTR, latency, revenue) are often estimated by sample means.  
- A/B tests compare estimators and ask whether differences are plausible under noise.  
- Regularization and Bayesian methods encode prior beliefs as probability structure.

---

## 3. Law of large numbers: why averages settle

**Law of large numbers (informal).** If $$X_1,X_2,\ldots$$ are i.i.d. with finite expectation $$\mu=\mathbb{E}[X_1]$$, then the sample mean

$$
\bar{X}_n=\frac1n\sum_{i=1}^n X_i
$$

converges to $$\mu$$ as $$n\to\infty$$ (in probability / almost surely under standard theorems).

**What this powers.** Polling, Monte Carlo integration, stochastic gradient noise averaging out, empirical frequencies approaching true probabilities. “Collect more data” is not a superstition; it is LLN in overalls—**when** the i.i.d. (or suitable ergodicity) assumptions approximately hold.

**What LLN is not.** It does not say every sequence looks typical early; it does not fix bias in the measuring instrument; it does not apply unchanged when the world drifts (nonstationarity) or samples are highly dependent.

---

## 4. Central limit theorem: why bells appear

**Central limit theorem (informal).** For i.i.d. $$X_i$$ with mean $$\mu$$ and finite variance $$\sigma^2>0$$,

$$
\sqrt{n}\,\frac{\bar{X}_n-\mu}{\sigma}
$$

converges in distribution to a standard normal $$N(0,1)$$ as $$n\to\infty$$.

**Mechanism.**  
*Sums of many small independent effects become approximately Gaussian; therefore sample means have approximately normal sampling distributions, enabling classical error bars.*

This is why introductory statistics is obsessed with $$z$$-scores and standard errors $$\sigma/\sqrt{n}$$: CLT supplies a universal approximation for the *distribution of the average*, not for the distribution of a single observation (which may be skewed, discrete, or heavy-tailed).

**Caution.** Heavy tails, dependence, and small $$n$$ break the fairy tale. Modern data science often uses bootstrap resampling and concentration inequalities (Hoeffding, Bernstein, …) as sharper or more flexible cousins.

---

## 5. Inference: from sample to statement

**Point estimation** produces a single guess $$\hat\theta$$ (sample mean for $$\mu$$, MLE for a model parameter). **Interval estimation** produces a set of plausible values with a calibrated frequency interpretation under a model (confidence intervals)—or a posterior credibility statement in Bayesian language.

**Hypothesis testing** formalizes “is this effect distinguishable from noise under a null model?” $$p$$-values are *not* “probability the null is true”; they are tail probabilities of a test statistic under the null. Misreading them is a cultural epidemic.

**Likelihood.** Given a parametric model $$p(x\mid\theta)$$, the likelihood $$L(\theta)=\prod_i p(x_i\mid\theta)$$ scores how well $$\theta$$ explains the sample. Maximum likelihood and Bayesian posteriors $$p(\theta\mid data)\propto L(\theta)p(\theta)$$ are two major inference philosophies sharing the same probabilistic grammar.

**Mechanism for technology.** Recommendation systems, credit models, medical risk scores, and A/B platforms all implement some pipeline of: model family → fit on sample → uncertainty-aware decision rule.

---

## 6. Machine learning risk: expected loss

In statistical learning theory, a prediction rule $$f$$ is judged by **risk**

$$
R(f)=\mathbb{E}\bigl[\ell(f(X),Y)\bigr],
$$

the expected loss on a random draw $$(X,Y)$$ from the true data distribution. You cannot compute $$R(f)$$ directly; you see only a sample and the **empirical risk**

$$
\hat{R}_n(f)=\frac1n\sum_{i=1}^n \ell(f(X_i),Y_i).
$$

**Empirical risk minimization (ERM)** chooses $$f$$ in a class $$\mathcal{F}$$ to minimize $$\hat{R}_n$$. Generalization theory studies when $$\hat{R}_n\approx R$$ uniformly over $$\mathcal{F}$$—VC dimension, Rademacher complexity, stability, PAC-Bayes, and modern double-descent stories all live here.

**Link.** Training neural nets with SGD is approximately stochastic optimization of empirical risk; probability explains *noise in gradients* and *gap between train and test*. See [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/) and [ML Theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/).

**Mechanism.**  
*“Accuracy on a dataset” is a sample; “performance in the wild” is a risk. Probability is the bridge—and the warning label.*

---

## 7. Dependence, Bayes, and decision under uncertainty

Real data are rarely neat i.i.d. coins:

- **Time series** and spatial data: dependence; CLT variants exist but naive SE formulas fail.  
- **Hierarchical / Bayesian models:** partial pooling; posterior predictive checks.  
- **Decision theory:** choose actions minimizing expected cost, not only estimating parameters.  
- **Calibration:** predicted probabilities should match empirical frequencies for trustworthy systems.

Bayes’ rule

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
$$

is the algebraic heart of updating beliefs. Spam filters, medical diagnosis prototypes, and many ranking systems are Bayesian networks or their learned cousins in spirit—even when implemented as neural nets outputting logits.

---

## 8. Causality, shift, and the ethics of uncertainty

**Correlation is not causation.** Observational association between ice cream sales and drowning does not mean ice cream causes drowning; temperature confounds both. Causal inference (potential outcomes, DAGs, instrumental variables) is probability with a surgery on interventions—not covered in depth here, but mandatory intellectual hygiene for data science claims.

**Distribution shift.** If production data $$P_{\mathrm{test}}$$ differs from training $$P_{\mathrm{train}}$$, risk guarantees transfer poorly. That is a probabilistic diagnosis of a very practical failure mode.

**Ethics.** Uncertainty communication matters: overconfident models harm. Fairness constraints, missing data mechanisms, and selection bias are probability-shaped moral-technical problems.

---

## 9. Concentration: modern finite-sample muscle

Beyond classical CLT, inequalities like Hoeffding’s bound give explicit finite-$$n$$ guarantees: for bounded i.i.d. variables, averages concentrate exponentially fast around their mean. These tools underwrite learning theory, randomized algorithms, and A/B platform power calculations.

The cultural shift from “$$n=30$$ therefore normal” to “state assumptions and use concentration / bootstrap / robust SEs” is the mark of a careful data scientist.

---

### Probability slogans (from video research)

Watch [3B1B Bayes](https://www.youtube.com/watch?v=HZGCoVF3YvM) and [Veritasium — The Bayesian trap](https://www.youtube.com/watch?v=R13BD8qKeTg) before the inference section.

- **Bayes hygiene:** always write the base rate; posterior odds = prior odds × likelihood ratio.
- **LLN vs CLT:** LLN says averages settle; CLT says *fluctuations* (properly scaled) look Gaussian.
- **ML risk** is an expectation; training error is one sample path of that expectation.

## Common confusions

| Claim | Correction |
|-------|------------|
| “Probability is only for casinos.” | It is the math of uncertainty in science, engineering, and ML. |
| “Law of large numbers means my small sample is already accurate.” | LLN is asymptotic; rates and variance matter. |
| “A $$p$$-value is $$P(\text{null true}\mid\mathrm{data})$$.” | No—that is a posterior; $$p$$-values are null-tail probabilities. |
| “Training loss equals true risk.” | Training loss is empirical; risk is expectation under the true law. |
| “More data always kills uncertainty.” | Bias, shift, dependence, and adversarial structure remain. |
| “The CLT says my data are normal.” | CLT is about the *mean’s sampling distribution*, not each $$X_i$$. |

---

## Exercises

1. **Warm-up.** A fair die is rolled. Compute $$\mathbb{E}[X]$$ and $$\mathrm{Var}(X)$$ for the face value $$X$$.  
2. **LLN narrative.** Explain in three sentences why polling averages stabilize as sample size grows—and name one assumption that can fail.  
3. **CLT use.** If i.i.d. measurements have $$\sigma=2$$, how does the SE of the mean scale from $$n=100$$ to $$n=400$$?  
4. **Risk vs empirical risk.** Write definitions of $$R(f)$$ and $$\hat{R}_n(f)$$ and one sentence on why minimizing the second is not automatically optimal for the first.  
5. **$$p$$-value literacy.** Rewrite a wrong popular sentence about $$p$$-values into a correct one.  
6. **Shift.** Give a real-world example where training and deployment distributions differ.  
7. **Stretch.** State Hoeffding’s inequality (look up if needed) and interpret the exponent’s dependence on $$n$$.

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/probability-data-science/`.

**Recommended order**

1. **CORE** — 3Blue1Brown — Bayes theorem (the geometry of Bayesian update): [https://www.youtube.com/watch?v=HZGCoVF3YvM](https://www.youtube.com/watch?v=HZGCoVF3YvM).
2. **FOUNDATION** — 3Blue1Brown — Binomial distributions | Probabilities of probabilities: [https://www.youtube.com/watch?v=8idr1WZ1A7Q](https://www.youtube.com/watch?v=8idr1WZ1A7Q).
3. **FOUNDATION** — Harvard Stat 110 (Blitzstein) — course / lecture portal: [https://stat110.net/](https://stat110.net/).
4. **FOUNDATION** — Harvard Stat 110 YouTube playlist: [https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo).
5. **ORIENTATION / hygiene** — Veritasium — The Bayesian trap (base rates): [https://www.youtube.com/watch?v=R13BD8qKeTg](https://www.youtube.com/watch?v=R13BD8qKeTg).
6. **ORIENTATION** — Khan Academy — Central limit theorem overview: [https://www.youtube.com/watch?v=YAlJCEDH2uY](https://www.youtube.com/watch?v=YAlJCEDH2uY).

Complete URL bibliography: `research/video-research/probability-data-science/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/probability-data-science/transcripts/` · status: `research/video-research/probability-data-science/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/probability-data-science_HZGCoVF3YvM_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/probability-data-science/references.md`.

### Videos (primary path)

1. 3Blue1Brown — Bayes theorem (the geometry of Bayesian update) — https://www.youtube.com/watch?v=HZGCoVF3YvM
2. 3Blue1Brown — Binomial distributions | Probabilities of probabilities — https://www.youtube.com/watch?v=8idr1WZ1A7Q
3. Harvard Stat 110 (Blitzstein) — course / lecture portal — https://stat110.net/
4. Harvard Stat 110 YouTube playlist — https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo
5. Veritasium — The Bayesian trap (base rates) — https://www.youtube.com/watch?v=R13BD8qKeTg
6. Khan Academy — Central limit theorem overview — https://www.youtube.com/watch?v=YAlJCEDH2uY
7. StatQuest — Maximum likelihood fundamentals — https://www.youtube.com/watch?v=XepXtl9YKwc
8. MIT 6.041 Probabilistic Systems Analysis (OCW) — https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/

### Videos (secondary finds)

9. 3Blue1Brown lockdown math / related probability episodes — https://www.3blue1brown.com/

### Papers, books, OCW, and web

10. Wasserman — All of Statistics (Springer): https://link.springer.com/book/10.1007/978-0-387-21736-9
11. Wikipedia — Law of large numbers: https://en.wikipedia.org/wiki/Law_of_large_numbers
12. Wikipedia — Central limit theorem: https://en.wikipedia.org/wiki/Central_limit_theorem
13. Wikipedia — Concentration inequality: https://en.wikipedia.org/wiki/Concentration_inequality
14. Blitzstein & Hwang — Introduction to Probability (Stat 110): https://stat110.net/

### Course

15. Course: [Linear Algebra → AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/), [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), [ML Theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/), [Math of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/). Pack: `research/video-research/probability-data-science/`.

## Further directions

- Next: [Number Theory → Cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/) (different “hardness” culture) or [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/) (how we minimize empirical risk).  
- Theory stretch: [ML Theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/).  
- Restate the core mechanism of this essay in one paragraph; note one precise question you still have.
