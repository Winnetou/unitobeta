from unittest import TestCase
from unitobeta import to_betacode, to_unicode

class UnibetaTest(TestCase):

    def setUp(self):
        self.unicode_text = """
        μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος
        οὐλομένην, ἣ μυρί᾽ Ἀχαιοῖς ἄλγε᾽ ἔθηκε,
        πολλὰς δ᾽ ἰφθίμους ψυχὰς Ἄϊδι προΐαψεν
        ἡρώων, αὐτοὺς δὲ ἑλώρια τεῦχε κύνεσσιν
        οἰωνοῖσί τε πᾶσι, Διὸς δ᾽ ἐτελείετο βουλή,
        ἐξ οὗ δὴ τὰ πρῶτα διαστήτην ἐρίσαντε
        Ἀτρεΐδης τε ἄναξ ἀνδρῶν καὶ δῖος Ἀχιλλεύς.
        τίς τ᾽ ἄρ σφωε θεῶν ἔριδι ξυνέηκε μάχεσθαι;
        Λητοῦς καὶ Διὸς υἱός: ὃ γὰρ βασιλῆϊ χολωθεὶς
        νοῦσον ἀνὰ στρατὸν ὄρσε κακήν, ὀλέκοντο δὲ λαοί,
        οὕνεκα τὸν Χρύσην ἠτίμασεν ἀρητῆρα
        Ἀτρεΐδης: ὃ γὰρ ἦλθε θοὰς ἐπὶ νῆας Ἀχαιῶν
        λυσόμενός τε θύγατρα φέρων τ᾽ ἀπερείσι᾽ ἄποινα,
        στέμματ᾽ ἔχων ἐν χερσὶν ἑκηβόλου Ἀπόλλωνος
        χρυσέῳ ἀνὰ σκήπτρῳ, καὶ λίσσετο πάντας Ἀχαιούς,
        Ἀτρεΐδα δὲ μάλιστα δύω, κοσμήτορε λαῶν:
        Ἀτρεΐδαι τε καὶ ἄλλοι ἐϋκνήμιδες Ἀχαιοί,
        ὑμῖν μὲν θεοὶ δοῖεν Ὀλύμπια δώματ᾽ ἔχοντες
        ἐκπέρσαι Πριάμοιο πόλιν, εὖ δ᾽ οἴκαδ᾽ ἱκέσθαι:
        παῖδα δ᾽ ἐμοὶ λύσαιτε φίλην, τὰ δ᾽ ἄποινα δέχεσθαι,
        ἁζόμενοι Διὸς υἱὸν ἑκηβόλον Ἀπόλλωνα.
        ἔνθ᾽ ἄλλοι μὲν πάντες ἐπευφήμησαν Ἀχαιοὶ
        αἰδεῖσθαί θ᾽ ἱερῆα καὶ ἀγλαὰ δέχθαι ἄποινα:
        ἀλλ᾽ οὐκ Ἀτρεΐδῃ Ἀγαμέμνονι ἥνδανε θυμῷ,
        ἀλλὰ κακῶς ἀφίει, κρατερὸν δ᾽ ἐπὶ μῦθον ἔτελλε:
        μή σε γέρον κοίλῃσιν ἐγὼ παρὰ νηυσὶ κιχείω
        ἢ νῦν δηθύνοντ᾽ ἢ ὕστερον αὖτις ἰόντα,
        μή νύ τοι οὐ χραίσμῃ σκῆπτρον καὶ στέμμα θεοῖο:
        τὴν δ᾽ ἐγὼ οὐ λύσω: πρίν μιν καὶ γῆρας ἔπεισιν
        ἡμετέρῳ ἐνὶ οἴκῳ ἐν Ἄργεϊ τηλόθι πάτρης
        ἱστὸν ἐποιχομένην καὶ ἐμὸν λέχος ἀντιόωσαν:
        ἀλλ᾽ ἴθι μή μ᾽ ἐρέθιζε σαώτερος ὥς κε νέηαι.
        """

        self.betacode_text = """
        mh=nin a)/eide qea\ *phlhi+a/dew *)axilh=os
        ou)lome/nhn, h(\ muri/' *)axaioi=s a)/lge' e)/qhke,
        polla\s d' i)fqi/mous yuxa\s *)/ai+di proi+/ayen
        h(rw/wn, au)tou\s de\ e(lw/ria teu=xe ku/nessin
        oi)wnoi=si/ te pa=si, *dio\s d' e)telei/eto boulh/,
        e)c ou(= dh\ ta\ prw=ta diasth/thn e)ri/sante
        *)atrei+/dhs te a)/nac a)ndrw=n kai\ di=os *)axilleu/s.
        ti/s t' a)/r sfwe qew=n e)/ridi cune/hke ma/xesqai;
        *lhtou=s kai\ *dio\s ui(o/s: o(\ ga\r basilh=i+ xolwqei\s
        nou=son a)na\ strato\n o)/rse kakh/n, o)le/konto de\ laoi/,
        ou(/neka to\n *xru/shn h)ti/masen a)rhth=ra
        *)atrei+/dhs: o(\ ga\r h)=lqe qoa\s e)pi\ nh=as *)axaiw=n
        luso/meno/s te qu/gatra fe/rwn t' a)perei/si' a)/poina,
        ste/mmat' e)/xwn e)n xersi\n e(khbo/lou *)apo/llwnos
        xruse/w| a)na\ skh/ptrw|, kai\ li/sseto pa/ntas *)axaiou/s,
        *)atrei+/da de\ ma/lista du/w, kosmh/tore law=n:
        *)atrei+/dai te kai\ a)/lloi e)u+knh/mides *)axaioi/,
        u(mi=n me\n qeoi\ doi=en *)olu/mpia dw/mat' e)/xontes
        e)kpe/rsai *pria/moio po/lin, eu)= d' oi)/kad' i(ke/sqai:
        pai=da d' e)moi\ lu/saite fi/lhn, ta\ d' a)/poina de/xesqai,
        a(zo/menoi *dio\s ui(o\n e(khbo/lon *)apo/llwna.
        e)/nq' a)/lloi me\n pa/ntes e)peufh/mhsan *)axaioi\
        ai)dei=sqai/ q' i(erh=a kai\ a)glaa\ de/xqai a)/poina:
        a)ll' ou)k *)atrei+/dh| *)agame/mnoni h(/ndane qumw=|,
        a)lla\ kakw=s a)fi/ei, kratero\n d' e)pi\ mu=qon e)/telle:
        mh/ se ge/ron koi/lh|sin e)gw\ para\ nhusi\ kixei/w
        h)\ nu=n dhqu/nont' h)\ u(/steron au)=tis i)o/nta,
        mh/ nu/ toi ou) xrai/smh| skh=ptron kai\ ste/mma qeoi=o:
        th\n d' e)gw\ ou) lu/sw: pri/n min kai\ gh=ras e)/peisin
        h(mete/rw| e)ni\ oi)/kw| e)n *)/argei+ thlo/qi pa/trhs
        i(sto\n e)poixome/nhn kai\ e)mo\n le/xos a)ntio/wsan:
        a)ll' i)/qi mh/ m' e)re/qize saw/teros w(/s ke ne/hai.
        """

    def test_to_betacode(self):

        expectations = self.betacode_text
        reality = to_betacode(self.unicode_text)
        self.assertEqual(reality, expectations)

    def test_to_unicode(self):

        expectations = self.unicode_text
        reality = to_unicode(self.betacode_text)
        self.assertEqual(reality, expectations)
