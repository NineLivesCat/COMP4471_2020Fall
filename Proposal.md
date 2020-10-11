# COMP4471_2020Fall

Team Member: CHEN, Sida; HUANG, Qiucan; LIN, Yifei

**What is the problem that you will be investigating? Why is it interesting?**  

we would like to utilizing GAN network to generate full-body image of anime-like characters. It is quite interesting because most reaserch are done in anime-like faces generation, but not full body. However, the body is also very important to impress anime viewers.

**What reading will you examine to provide context and background?**  

We found some useful paper talking about how to generate anime-like faces, which could be very close to full-body generation. Most of them utilize GAN network to gerenate and then discriminate the generated work from real work. Some other articals talking about style trasfer which could also be helpful.

[Full-body High-resolution Anime Generation with Progressive Structure-conditional Generative Adversarial Networks](https://arxiv.org/pdf/1809.01890.pdf)  
[Progressive growing of GANs for imrpoved quality, stability, and variation](https://arxiv.org/pdf/1710.10196.pdf)  
[A Style-Based Generator Architecture for Generative Adversarial Networks](https://arxiv.org/pdf/1812.04948.pdf)  
[Multi-Human-Parsing (MHP)](https://github.com/ZhaoJ9014/Multi-Human-Parsing)  
[Making Anime Faces With StyleGAN](https://www.gwern.net/Faces#)  

**What data will you use? If you are collecting new data, how will you do it?**  

We found some dataset but it is kind of old-fashioned. We will keep trying to find more data sets as possible. If we cannot find satisfying data sets, we can use scripts to collect figures from internet.

[Manga109](http://www.manga109.org/en/)  

**What method or algorithm are you proposing? If there are existing implementations, will you use them and how? How do you plan to improve or modify such implementations? You don't have to have an exact answer at this point, but you should have a general sense of how you will approach the problem you are working on.**

We plan to use GAN network. They use a network to generate the details on faces, and another network to classify whether it is a true one or fake one. We will definitely learn from this model, but also modify it a little bit. We plan to use two different networks to generate faces and bodies separately, and then use another network to distinguish them together.

**How will you evaluate your results? Qualitatively, what kind of results do you expect (e.g. plots or figures)? Quantitatively, what kind of analysis will you use to evaluate and/or compare your results (e.g. what performance metrics or statistical tests)?** 

Our network need to generate figures that are similar to real anime characters. The similarity and rationality is the most important criteria. Quantitatively, it depends on the network. Currently we don't have a concrete idea, we are reading some papers and implementations about our topic in order to learn more about it.