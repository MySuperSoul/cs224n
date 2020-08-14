1.
(a)

i. The parameter $m$ will keep the track of last direction of the gradient descent, and helps to counteract the current part of direction which not the true direction, and strengthen the true direction of the gradient descent.

ii. Positions which the computing gradients are low will get corresponding larger updates.

Reasons about helping: Since the gradients calculated are different, some of the positions are higher, some of are lower. In this way, the learning rate is self adjusted by the gradients, and the model will converge faster.

(b)

i. 

$$
\mathbb{E}_{p_{\text {drop }}}\left[\mathbf{h}_{d r o p}\right]_{i}=h_{i} \implies \gamma(1-p_{drop})h_i = h_i \implies \gamma = \frac{1}{1-p_{drop}}
$$

ii.

Training: As a regulation method, generalize the model
Testing: Since the droping procedue is random, this will cause different evaluation results when you perform multiple testing.

2.
(a)

| Stack | Buffer | New Dependency | Transition |
| -- | -- | -- | -- |
| [Root] | [I, parsed, this, sentence, correctly] | | Initial |
| [Root,I] | [parsed, this, sentence, correctly] | | SHIFT |
| [Root,I,parsed] | [this, sentence, correctly] | | SHIFT |
| [Root,parsed] | [this, sentence, correctly] | parsed->I | LEFT-ARC |
| [Root,parsed,this] | [sentence, correctly] | | SHIFT |
| [Root,parsed,this,sentence] | [correctly] | | SHIFT |
| [Root,parsed,sentence] | [correctly] | sentence->this | LEFT-ARC |
| [Root,parsed] | [correctly] | parsed->sentence | RIGHT-ARC |
| [Root,parsed,correctly] | | | SHIFT |
| [Root,parsed] | | parsed->correctly | RIGHT-ARC |
| [Root] | | Root->parsed | RIGHT-ARC |

(b)

$2n$ steps. Because initial is [Root], and the end state also is [Root]. We need `SHIFT` $n$ times to push elements in, and $n$ times to pop the elements out, so totally $2n$ steps.