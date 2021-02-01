---
layout: post
title:  Areas of CS to Emerge in the Next 10 Years
date:   2021-02-01
description: .
---


As an undergraduate student primarily majoring in CS, I've been recently thinking 

Note that these are just my personal opinions.

<hr>

## Artificial Intelligence

It has been slighty less than a decade since the era of AI has started.  Despite of enormous contributions, there are still much to be studied, even for the pure theoretical fields. The ultimate goal of the related research areas would be abilities to build machines that outperforms human performance.


#### A Transition of DL Framework

The most widely spreaded approach for DL is definetely the supervised learning field, where theinputs and targeted outputs are given, and the task is defined to fine the model that achieves the highest performance based on the given measures. The development of some widely-used popular DL models have been adapted into numerous application stacks.

Despite of its affect and contributions, the critical point still remains. The 

of supervised learning comes from

1 initial efforts for collecting datasets
2 cannot effectively corporate with unseen data or untrained data, which steadily shows gap between application level. 

As the general methods for applying active, incremental learning shows up, the whole major pipeline of learning technique will likely to be transformed. 

Active Learning, Incremental Learning

강화학습과 큰 틀에서는 유사하고, 강화학습의 technique들이 take place할 수 있는 부분.

이런 부분에서 general한 approach가 나오지는 않았으나, 조만간 널리 적용되는 방법이 연구될 것임. 이런 general한 approach는 향후 

#### AI for Multi & Varying Input Sources

Multimodal

data source가 시시각각 변하는 와중에서도, robust한 판단을 내릴 수 있거나, uncertainty에 대한 management가 가능한 ai. 

#### Universal Knowledge Management & Modulized Knowledge

NLP is a core in the web

Somewhere between embedding knowledge with DL and dealing with Graph

Automated bot to search for web may be an idea

#### Correctness Proof of the Developed AI

결과적으로 이것을 사람이 믿을 수 있느냐 없느냐의 문제로 귀결된다.
AI 법률 시스템이나, 

explainable AI는 이 것을 위한 하나의 거쳐가는 step이지만, 설명하는 것과 맞고 틀리는 것을 증명하는 것은 전혀 다른 문제이다. 이 방식이 진행되어야만 

## Data Systems

#### Streaming Data & Signal Processing


How?


#### Leveraging Automation in Building / Managing Computer Systems



#### An Unified Solution for Controlling Super-Large Scale Systems

is parallelism the answer?

<hr>

## Web / Cloud / OS

#### Embedding the Web into OS

chrome OS나 구글이 만들고 있는 os 

브라우저는 더 많은 일을 할수록 개발되어 가고 있다.

이 흐름에 맞춰, 일반 사용자의 프로세스를 봤을 때, 브라우저 하나가 차지하는 비중은 옛날에 비해 더 늘아기고 있고, 앞으로 더 늘어날 것이다. 

이 추세에 맞춰 요즘 많은 application은 웹앱으로 개발되고 있는데, 이는 곧 이러한 os에서도 프로그램의 사용이 완전히 가능하다는 것이다. 심지어, 일반 사용자들이 가장 많이 사용하는 엑셀, 파워포인트 등도 요즘은 인터넷으로도 쉽게 작업할 수 있다. 

물론 이러한 흐름의 가장 중요한 단점과 전제는, 인터넷이 끊기는 순간 컴퓨터가 무기력해진다는 점에 있다. 이 부분은 새로운 개념의 infrastructure가 필요하다. 단순히 5g가 아니라, 어디서든 "저렴한" 인터넷이 되어야 함.

이 시스템이 보급된다면, 복잡한 컴퓨테이션은 서버를 쓰는 편이 관리하는 개발자 입장에서 더 편리할 경우가 생길 것이므로, 클라우드와의 접목은 당연히 예견된다.

게이밍 목적이나, 특별한 프로그램들을 돌리기에는 아직 갈 길이 멀고, 이 기술이 전체 컴퓨터 시장을 장악하는 데에는 향후 몇십 년 정도는 걸릴 일이라고 본다. 그러나 personal computer와 smartphone에는 무조건 적용될 것이며, 생각했던 것 보다 빠르게 다가올 수 있다.

#### Massive Cloud Computing Development

위와 연계되어, 사용자의 job을 대부분 클라우드에서 처리하게 될 것이다. 개발자 입장에서도 product launch를 위한 tech stack을 최소한 정형화시고 단순화시킬 수 있으며, cross platform, cross device developement의 번거로움을 완벽하게 해결하려면, 결국에는 cloud의 의존도가 올라갈 것이다.

그렇다고 하여, cloud 컴퓨팅 분야에서 단기간에 무언가 특별하고 혁신적인 개선이 이뤄질 것으로 보이지는 않는다. 이미 kubernetes와 같은 cluster orchstrization 기술은 충분히 제 기능을 하고 있다고 보인다. 하지만, 더 혁신적인 방법이 있을 수 있는데, 이러한 문제들에 대해서는 클라우드 센터를 운영하는 기업들이 잘 알고 있을 것이다. 

다만, 클라우드 운영의 비용(전기료, disk 등의 소모성 자원에 대한 management) 절감과 관련된 방향으로 반도체, 프로세서 설계, 네트워크 스위치 등 모든 하위 세부 기술이 이 방향과 관해 쏠릴 것이며, 궁극적으로 클라우드 서비스의 영향력은 세지지만 이를 이용하는 데 있어 부담은 더 줄어들 것이다.

#### Completely Automated Web Service Development

even for the backend, and security.

개발자의 다수는 web에 포진하고 있다.

웹은 복잡하지만(sucks) 단순함.

웹을 잠깐 배울 기회가 있었는데, 그 가치에 비해 너무 복잡한 것들이 많고, 개발 방법이 발전하는 속도가 너무 빨라 정신이 없고, 한 개발을 위해 개발자들이 공부할 것이 아주 많다. (아주 특이한 분야인 듯 하다.)

물론 대기업의 웹은 엄청 복잡하지만

대부분의 기업들의 웹사이트는 기능 상으로는 크게 발전하는 것이 없음.
아무리 복잡한 정도라고 해 봐야 상품 거래 정도?

하지만, 이런 것 역시 크게 보면 정형화된 pipeline으로 정리할 수 있음.
오히려, 각 경우에 따른 통합적인 솔루션이 나온다면,

기능 추가를 통해 사용자 경험에 대한 pipeline을 제공하면 시스템을 자동으로 구축할 것임.

지금 존재하는 여러 no-coding 웹 개발 시스템들은 있긴 하지만, 아직 약하고 정말 일부 기능뿐 만 제공할 뿐 더러, 아직 백엔드 자동화를 해 주는 시스템은 없다고 봐도 된다.

웹의 비중이 커지는 것은 맞지만, 오히려 케이스들은 일반화될 것이다. 
향후 더 빠르 처리 방식들이 개발되어 나온다면, 신규 개발을 할 필요 없이, 자동으로 백엔드 시스템 업데이트 만으로 최신 기술을 유지할 수 있다. 

이러한 어프로치는 보안 취약성 약화나, 취약점 발견 시 더 빠르게 업데이트 될 수 있다는 점에서 향후 보안 업계에서 할 일을 많이 줄여줄 것이라고 본다.

이러한 웹 기술과 방향성은, 향후 다른 development의 영역, 예를 들면 공장 모니터링이라던지, 컴퓨터가 필요한, 정형화되면서 간단한 사용자 인터페이스를 요구하는 곳으로  빠르게 퍼져나갈 수 있음. 또한, 개발자들이나 관리자들을 위한 만능 Interface ( data input/source connector만 지정해주면 자동으로 visualization 해 주고, 간단한 feedback을 처리할 수 있는) visualization tool 역시 관련되어서 성장할 가능성이 있다.

결과적으로 naive한 웹 개발자들의 수요는 줄 것임이 분명하다. 차라리, 웹 그래픽스나 렌더링 관련 혹은 웹 디자이너가 되는 것이 낫다.

<hr>


## Combination with Other Science Fields

#### Strong Influnce in Biology

두말해봤자이다.

융합적 능력이 가장 빛을 발휘하는 때가 아닐까 싶다.

old-fashioned 연구방식을 바꿀 것임.

#### Building Block of the Finance's Future


두말해봤자이다.
알고리즘 뿐 아니라, 사용자 레벨에서 재정 / 경제 관련 전반을 컴퓨터 기술에 의존하는 시대가 올 것이다.

비트코인이야 두말할 것도 없고,

당장 조만간을 보더라도 개인 사용자들의 알고리즘 트레이딩도 늘어날 것임.

여기서는 수학도 아주 중요한데, handling uncertainty와 같은 numerical methods가 엄청난 힘을 쓸 수 있다.


#### 3D Technology along with AR

<hr>


## Hardwares

#### All Tech Stacks For Managing Devices Connected via Internet

much general than IoT?

#### Neuromorphic Processors

for changing neuron structures?

## Conclusion

더이상 컴퓨터 공학이 그 자체로 stand할 수 있는 시대는 지났다, 산업에 적용될 수 없는 기술은 바로바로 도태되어야 된다고 보며, 대규모 처리가 가능한 컴퓨터 공학이 사용자의 관점에서 어떻게 쓰일 수 있는지를 연구하는 것이 mainstream이 될 것이다.

사실 이 과정에서는 많은 경우 전자과의 개입이 필수적이다. 따라서 전자과는 컴퓨팅 자체만을 하는 것 보다 더 promising하고, 컴퓨터를 하는 사람들 역시 그 과정에서는 전자과와의 협업과 discussion을 통한 기술 개발에 더 힘을 실어야 될 것이라고 본다.