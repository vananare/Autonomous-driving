import matplotlib.pyplot as plt

history = {'loss': [14.56086595991687, 0.7930556596705354, 0.46522495021697624, 0.3093251507885917, 0.22626448037155358, 0.199500991682809, 0.19103259089818703, 0.2933192140362788, 0.2113210599519562, 0.18892318086387386, 0.22282025044037504, 0.40542291906640476, 0.6599102961080384, 0.19532744010190214, 0.18251837405835603, 0.17209411721637927, 0.1642562260985337, 0.16060585382160547, 0.1561811744766295, 0.15521087437697614, 0.1939439835421396, 0.16007142400734836, 0.1506740808094881, 0.1484876848978326, 0.14473591503785588, 0.1416964361821056, 0.1401185283123626, 0.13645846038628537, 0.13421391943710528, 0.12931161370619582, 0.12490566287084645, 0.11979493034950013, 0.11684183143014847, 0.11081427724401507, 0.10616875145368242, 0.10126200635303377, 0.09684508868967474], 'val_output_Throttle_loss': [0.21770959909794466, 0.3031166397070266, 0.2057225051388707, 0.1810863192746732, 0.15888892667904003, 0.1188994198859085, 0.11263898045955394, 0.1182300998589885, 0.11511831658974546, 0.11104255818263573, 0.11164010501450285, 0.11124858541903312, 0.11052366022965354, 0.11018817281329867, 0.10910036960326837, 0.10516345876863158, 0.10218338588368359, 0.1016470312816817, 0.13948707496923096, 0.10265640872852866, 0.10423633963564058, 0.09870118767492789, 0.09836403976964903, 0.09628938824206958, 0.09789648403794106, 0.09964115250888002, 0.0986894419484431, 0.09757986651556422, 0.09396980844254135, 0.09841983794014653, 0.09880238698554476, 0.09578101798462808, 0.09477009718013832, 0.09541298462362484, 0.09653205442208553, 0.10046487179946145, 0.10256137545986417], 'val_output_Brake_loss': [0.2172334685692133, 0.19885397965426477, 0.13009892965377526, 0.06932420075630051, 0.031023841260999035, 0.013943989880025806, 0.008152086229805941, 0.005308776155273782, 0.004576595887801929, 0.004180869981878287, 0.004343764688023152, 0.004665605482541479, 0.004206651423404408, 0.004121187388006562, 0.004027801591821078, 0.004004742334140641, 0.004035653490413491, 0.0040304001893808694, 0.004242387507595827, 0.003990239510454141, 0.004037591891102359, 0.004013846015159331, 0.0040886032658085224, 0.004033701581126376, 0.0040046082194631055, 0.003993322498589449, 0.004086382153563252, 0.0040221338219478915, 0.004011049092272963, 0.004090073512051028, 0.0041071315950650285, 0.004118449953331414, 0.004055259110307876, 0.004037380399864251, 0.004008787815961674, 0.004009774273162344, 0.004052408063770689], 'val_output_Steer_loss': [0.030887987798990935, 0.027857938309025786, 0.022172822089023256, 0.02269128366514717, 0.047932113390262834, 0.010049390709776364, 0.012929699798148233, 0.014208340121034831, 0.015018164994349924, 0.012181847500626522, 0.013696188319209842, 0.014030633325572936, 0.01381538713529953, 0.012971531337954284, 0.010238370536455476, 0.009585143425376913, 0.008900664177063037, 0.010657122621510669, 0.02059882139083708, 0.008805167831628392, 0.01935182702216926, 0.008852700608115638, 0.00867605778570569, 0.00901769734483404, 0.008596912767107761, 0.008944244998422576, 0.008851572326916033, 0.00878971221235868, 0.008773165709559582, 0.010744584433635556, 0.008456911420987602, 0.008344145313679358, 0.008589199445331583, 0.007912864185718967, 0.009097230845421545, 0.008806222433182116, 0.008500896142248473], 'output_Throttle_loss': [4.382307643266103, 0.35083060066090294, 0.2534466600556079, 0.2051635084712423, 0.17199495491438396, 0.15647616643312884, 0.15087514270385485, 0.15731909103714378, 0.159247073262237, 0.15456229958885476, 0.152151657911818, 0.1589203217924791, 0.16830320081564767, 0.15198329447740377, 0.14796803646864437, 0.1411194903599475, 0.13563868611136043, 0.13245619021604177, 0.12906600887656208, 0.1272279344782374, 0.14193381330558705, 0.12878897312127485, 0.12476826927098264, 0.12258322790134728, 0.11984226815630505, 0.11708882157410783, 0.11485888166828928, 0.11211819558921347, 0.10908114467598815, 0.10526958390579179, 0.10124887485478912, 0.09706173069673993, 0.09325810056923234, 0.08857534624742242, 0.08388664349732686, 0.07871376603723818, 0.07483227717422024], 'output_Steer_loss': [6.530309646076633, 0.2617308491054861, 0.1280954557006555, 0.0666473001081094, 0.03748249292279236, 0.03288410295363185, 0.031805485273112145, 0.10130280857207377, 0.04463870550413719, 0.028361417968387915, 0.059900465465650046, 0.2031290550746417, 0.3572063365168606, 0.03655059482787159, 0.02831676781863668, 0.02500036237349603, 0.022828869074547273, 0.022392906258099095, 0.021357410761242163, 0.022218342165739865, 0.04525103254581338, 0.02533011473813196, 0.02015014891587504, 0.020156607588613023, 0.019131907134425842, 0.018845443445345635, 0.019490383514842672, 0.01858061047543516, 0.019378969339430684, 0.018274191766760463, 0.017893861464012308, 0.01696026693636335, 0.017812521013395873, 0.01646264026669257, 0.016501853654314808, 0.01677073079701974, 0.01620674583689915], 'val_loss': [0.46583105613178805, 0.5298285581927114, 0.357994256268765, 0.27310180387301547, 0.23784488178174593, 0.1428928009106971, 0.13372076636307678, 0.13774721571661638, 0.1347130773420707, 0.12740527567885299, 0.12968005776069474, 0.12994482408481967, 0.12854569870099988, 0.12728089137433343, 0.12336654166972709, 0.11875334440257987, 0.11511970350569892, 0.11633455429216825, 0.16432828352707526, 0.11545181601245273, 0.1276257587820544, 0.11156773411947245, 0.11112870101320402, 0.10934078734797642, 0.11049800477935004, 0.11257871984122725, 0.11162739633769922, 0.11039171264647453, 0.10675402309730861, 0.11325449568673475, 0.11136642970997752, 0.10824361319114445, 0.10741455565001606, 0.1073632293682406, 0.10963807292322393, 0.11328086886759645, 0.11511467962132746], 'output_Brake_loss': [3.648248764997058, 0.1804942106634791, 0.08368283392020867, 0.03751434198087017, 0.016787032153657646, 0.010140722363247307, 0.008351963164730351, 0.03469731332786696, 0.007435281043259415, 0.005999463337543334, 0.010768126523176333, 0.04337354225263435, 0.1344007600288573, 0.0067935507698192125, 0.006233569948814641, 0.00597426459459836, 0.005788670790053282, 0.005756757077758032, 0.005757754618133392, 0.005764597626130358, 0.006759137446990252, 0.0059523361945658555, 0.005755662818257441, 0.0057478494963111, 0.005761739525919083, 0.005762171050023152, 0.005769263370474241, 0.00575965418274302, 0.005753805716899524, 0.0057678380360114325, 0.00576292650831449, 0.00577293282364027, 0.005771209850349416, 0.005776290872303044, 0.005780254533204883, 0.005777509666028323, 0.005806065448181173]}


keys = []
for key, values in history.iteritems():
    plt.plot(values)
    keys.append(key)
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(keys, loc='upper right')
plt.show()