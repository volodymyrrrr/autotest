import time

import gspread
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from pages.page_list import PageList

client = gspread.service_account('gs_credentials.json')
working_sheet = client.open_by_url(
    'https://docs.google.com/spreadsheets/d/1fRi9qAdb-E-xAY_jQiMdjjEsN1xZZdxK6865V-Ck6RE/edit#gid=0')
wb1 = working_sheet.get_worksheet(0)
URLS = wb1.get_values('B2:C7')
print(URLS)
for user in list1:
    with open("results.csv", "a", newline='') as file2:
        writer2 = csv.writer(file2, delimiter=";")
        writer2.writerow(
            user
        )


        class TestForm:

            def test_Bellroy(self, driver, ):
                page_list = PageList(driver, wb1.acell('B2').value)
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Bellroy", "pass"))
                except:
                    list1.append(("Bellroy", "false"))

            def test_Shaneco(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.shaneco.com/design-your-own-necklace/dyo-fashion-necklaces/vintage-diamond-pendant-in-14k-rose-gold-20-in/p/41082847')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Shaneco", "pass"))
                except:
                    list1.append(("Shaneco", "false"))

            def test_Katespade(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.katespade.com/products/the-little-better-sam-nylon-medium-backpack/K4467.html?cgid=ks-handbags-view-all')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Katespade", "pass"))
                except:
                    list1.append(("Katespade", "false"))

            def test_LivingSpaces(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.livingspaces.com/pdp-capri-ii-outdoor-dining-chair-258740')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.living_space()
                    list1.append(("LivingSpaces", "pass"))
                except:
                    list1.append(("LivingSpaces", "false"))
                print(list1)

            def test_Hipvan(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.hipvan.com/products/abby-4-seater-lounge-sofa-pearl')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Hipvan", "pass"))
                except:
                    list1.append(("Hipvan", "false"))

            def test_Novica(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.novica.com/p/tropical-ceramic-sea-turtle-wall-art-from/261664/')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Novican", "pass"))
                except:
                    list1.append(("Novica", "false"))

            def test_Hsamuel(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.hsamuel.co.uk/webstore/d/1267779/HUGO+%23FIRST+Men%27s+Black+IP+Bracelet+Watch/')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "cookie-consent-dialog__cta").click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_tangiblee_button()
                    list1.append(("Hsamuel", "pass"))
                except:
                    list1.append(("Hsamuel", "false"))
                print(list1)

            def test_CitizenWatches(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.citizenwatch.com/us/en/product/BN0231-01L.html')
                page_list.open()
                time.sleep(2)
                # driver.find_element(By.CLASS_NAME, "kl-private-reset-css-Xuajs1").click()
                page_list.scroll()
                time.sleep(3)
                try:
                    page_list.find_cta()
                    list1.append(("CitizenWatches", "pass"))
                except:
                    list1.append(("CitizenWatches", "false"))

            def test_Samsonite(self, driver, ):
                page_list = PageList(driver,
                                     'https://shop.samsonite.com/luggage/carry-on-luggage/black-label-cosmolite-3.0-carry-on-spinner/80407XXXX.html?dwvar_80407XXXX_color=804071726&cgidmaster=lugaz#')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_tangiblee_button()
                    list1.append(("Samsonite", "pass"))
                except:
                    list1.append(("Samsonite", "false"))

            def test_Ernestjones(self, driver, ):
                page_list = PageList(driver,
                                     "https://www.ernestjones.co.uk/webstore/d/1566180/omega+seamaster+aqua+terra+ladies'+green+leather+strap+watch/")
                page_list.open()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, 'js-close-dialog').click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_tangiblee_button()
                    list1.append(("Ernestjones", "pass"))
                except:
                    list1.append(("Ernestjones", "false"))

            def test_R1800Lighting(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.1800lighting.com/hinkley-lighting-fletcher-13-inch-large-pendant-CP71511.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("R1800Lighting", "pass"))
                except:
                    list1.append(("R1800Lighting", "false"))

            def test_Fossil(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.fossil.com/en-us/products/bronson-chronograph-black-eco-leather-watch/FS5874.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Fossil", "pass"))
                except:
                    list1.append(("Fossil", "false"))

            def test_Galleryfurniture(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.galleryfurniture.com/yellowstone-dutton-coffee-table-201764594.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Galleryfurniture", "pass"))
                except:
                    list1.append(("Galleryfurniture", "false"))

            def test_Colemanfurniture(self, driver, ):
                page_list = PageList(driver,
                                     'https://colemanfurniture.com/bajo-pink-lacquer-desk.htm')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "klaviyo-close-form").click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_tangiblee_btn()
                    list1.append(("Colemanfurniture", "pass"))
                except:
                    list1.append(("Colemanfurniture", "false"))

            def test_Bulgari(self, driver, ):
                page_list = PageList(driver,
                                     'http://www.bulgari.com/en-us/products/282911-e.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Bulgari", "pass"))
                except:
                    list1.append(("Bulgari", "false"))

            def test_Grayandsons(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.grayandsons.com/s518841-heavy-and-bright-diamond-bracelet.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_tangiblee_button()
                    list1.append(("Grayandsons", "pass"))
                except:
                    list1.append(("Grayandsons", "false"))

            def test_Golfco(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.golfco.co.il/8347020122')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Golfco", "pass"))
                except:
                    list1.append(("Golfco", "false"))

            def test_Fhinds(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.fhinds.co.uk/jewellery/gold-and-silver-jewellery/necklaces-and-lockets/9ct-Rose-Gold-Cubic-Zirconia-Heart-Necklace-R6969?utm_source=google&amp;utm_medium=product+search')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Fhinds", "pass"))
                except:
                    list1.append(("Fhinds", "false"))

            def test_Jared(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.jared.com/diamond-bridal-set-1-ct-tw-princess-14k-white-gold/p/V-993758200')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_js_product_tangiblee()
                    list1.append(("Jared", "pass"))
                except:
                    list1.append(("Jared", "false"))

            def test_Kay(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.kay.com/diamond-accent-ring-sterling-silver/p/V-580895605')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_js_product_tangiblee()
                    list1.append(("Kay", "pass"))
                except:
                    list1.append(("Kay", "false"))

            def test_Kipling(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.kipling-usa.com/maisie-diaper-backpack/BP4426.html?dwvar_BP4426_color=933')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.XPATH, '//*[@id="monetate_lightbox_contentMap"]/area[1]').click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Kipling", "pass"))
                except:
                    list1.append(("Kipling", "false"))

            def test_Apt2b(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.apt2b.com/collections/all-beds/products/forman-queen-platform-bed')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Apt2b", "pass"))
                except:
                    list1.append(("Apt2b", "false"))

            def test_Jtv(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.jtv.com/product/red-sponge-coral-silver-bracelet/SWE924?N=1334837086')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Jtv", "pass"))
                except:
                    list1.append(("Jtv", "false"))

            def test_Zales(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.zales.com/previously-owned-2-ct-tw-diamond-frame-bridal-set-14k-white-gold/p/V-33730955')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_js_product_tangiblee()
                    list1.append(("Zales", "pass"))
                except:
                    list1.append(("Zales", "false"))

            def test_Us_En_Aldoshoes(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.aldoshoes.com/us/en_US/legioraa-medium-blue/p/13372772')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Us_En_Aldoshoes", "pass"))
                except:
                    list1.append(("Us_En_Aldoshoes", "false"))
                print(list1)

            def test_Ca_En_Aldoshoes(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.aldoshoes.com/ca/en//c/p/13305876')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Ca_En_Aldoshoes", "pass"))
                except:
                    list1.append(("Ca_En_Aldoshoes", "false"))
                print(list1)

            def test_Ca_Fr_Aldoshoes(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.aldoshoes.com/ca/fr//c/p/13261123')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Ca_Fr_Aldoshoes", "pass"))
                except:
                    list1.append(("Ca_Fr_Aldoshoes", "false"))
                print(list1)

            def test_Us_En_Callitspring(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.callitspring.com/us/en_US/women/handbags/weaved-black/p/13217133')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Us_En_Callitspring", "pass"))
                except:
                    list1.append(("Us_En_Callitspring", "false"))

            def test_Ca_En_Callitspring(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.callitspring.com/ca/en/c/p/13512492')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Ca_En_Callitspring", "pass"))
                except:
                    list1.append(("Ca_En_Callitspring", "false"))

            def test_Ca_En_Globoshoes(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.globoshoes.com/ca/en/c/p/13449809')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "c-modal__icon-close")
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Ca_En_Globoshoes", "pass"))
                except:
                    list1.append(("Ca_En_Globoshoes", "false"))

            def test_Fantasiasmiguel(self, driver, ):
                page_list = PageList(driver,
                                     'https://tienda.fantasiasmiguel.com/products/6626-2014')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "klaviyo-close-form").click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Fantasiasmiguel", "pass"))
                except:
                    list1.append(("Fantasiasmiguel", "false"))

            def test_Jewlr_com(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.jewlr.com/products/JWLB0061/10k-rose-gold-birthstone-bar-bracelet-with-1-5-stones-and-cubic-zirconia-stone?sku=10KR')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Jewlr_com", "pass"))
                except:
                    list1.append(("Jewlr_com", "false"))

            def test_Ca_En_Swissgear(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.swissgear.ca/en/swiss-watches/swissgear-legacy-watch-black-with-black-dial-light-brown-strap-ca')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "klaviyo-close-form").click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_tangiblee_button()
                    list1.append(("Ca_En_Swissgear", "pass"))
                except:
                    list1.append(("Ca_En_Swissgear", "false"))

            def test_Ca_Fr_Swissgear(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.swissgear.ca/fr/swiss-watches/swissgear-legacy-watch-silver-with-cream-dial-dark-brown-strap-ca')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "klaviyo-close-form").click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_tangiblee_button()
                    list1.append(("Ca_Fr_Swissgear", "pass"))
                except:
                    list1.append(("Ca_Fr_Swissgear", "false"))

            def test_Jewlr_com_au(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.jewlr.com.au/products/JWLB0061/sterling-silver-birthstone-bar-bracelet-with-1-5-stones-and-cubic-zirconia-stone?sku=SS')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Jewlr_com_au", "pass"))
                except:
                    list1.append(("Jewlr_com_au", "false"))

            def test_Jewlr_co_uk(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.jewlr.co.uk/products/JWLB0061/9k-rose-gold-birthstone-bar-bracelet-with-1-5-stones-and-cubic-zirconia-stone?sku=10KR')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Jewlr_co_uk", "pass"))
                except:
                    list1.append(("Jewlr_co_uk", "false"))

            def test_Jewlr_ca(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.jewlr.ca/products/JWLB0061/10k-rose-gold-birthstone-bar-bracelet-with-1-5-stones-and-cubic-zirconia-stone?sku=10KR')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Jewlr_ca", "pass"))
                except:
                    list1.append(("Jewlr_ca", "false"))

            def test_Tacori(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.tacori.com/wedding-ring-blooming-beauties-ht2522/')
                page_list.open()
                time.sleep(10)
                driver.find_element(By.CLASS_NAME, "leadinModal-close").click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_tangiblee_btn()
                    list1.append(("Tacori", "pass"))
                except:
                    list1.append(("Tacori", "false"))

            def test_Ca_En_Fossil(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.fossil.com/en-ca/products/neutra-chronograph-brown-leather-watch/FS5380.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Ca_En_Fossil", "pass"))
                except:
                    list1.append(("Ca_En_Fossil", "false"))

            def test_Ca_Fr_Fossil(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.fossil.com/fr-ca/products/montre-chronographe-en-acier-inoxydable-de-ton-or-bronson/FS5877.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Ca_Fr_Fossil", "pass"))
                except:
                    list1.append(("Ca_Fr_Fossil", "false"))

            def test_Uk_En_Fossil(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.fossil.com/en-gb/products/hybrid-smartwatch-hr-neutra-brown-leather/FTW7025.html')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "bx-row-submit-no").click()
                driver.find_element(By.ID, "consent-tracking-button").click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Uk_En_Fossil", "pass"))
                except:
                    list1.append(("Uk_En_Fossil", "false"))

            def test_Fr_Fr_Fossil(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.fossil.com/fr-fr/products/montre-connectee-hybride%C2%A0hr-neutra-en-cuir-brun/FTW7025.html')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "bx-row-submit-no").click()
                driver.find_element(By.ID, "consent-tracking-button").click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Fr_Fr_Fossil", "pass"))
                except:
                    list1.append(("Fr_Fr_Fossil", "false"))

            def test_De_De_Fossil(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.fossil.com/de-de/products/hybrid-smartwatch-hr-collider-leder-kautschuk-dunkelbraun/FTW7008.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("De_De_Fossil", "pass"))
                except:
                    list1.append(("De_De_Fossil", "false"))

            def test_It_It_Fossil(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.fossil.com/it-it/products/orologio-fb-01-a-tre-sfere-in-acciaio-color-oro-rosa-con-datario/ES4748.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("It_It_Fossil", "pass"))
                except:
                    list1.append(("It_It_Fossil", "false"))

            def test_Jp_Ja_Fossil(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.fossil.com/ja-jp/products/jacueline-%E3%83%AD%E3%83%BC%E3%82%BA%E3%82%B4%E3%83%BC%E3%83%AB%E3%83%89%E3%83%88%E3%83%BC%E3%83%B3%E3%82%B9%E3%83%86%E3%83%B3%E3%83%AC%E3%82%B9%E3%82%B9%E3%83%81%E3%83%BC%E3%83%AB-%E3%83%8F%E3%82%A4%E3%83%96%E3%83%AA%E3%83%83%E3%83%89%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%82%A6%E3%82%A9%E3%83%83%E3%83%81/FTW5018.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Jp_Ja_Fossil", "pass"))
                except:
                    list1.append(("Jp_Ja_Fossil", "false"))

            def test_Au_En_Fossil(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.fossil.com/en-au/products/scarlette-mini-three-hand-date-two-tone-stainless-steel-watch/ES4949.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Au_En_Fossil", "pass"))
                except:
                    list1.append(("Au_En_Fossil", "false"))

            def test_In_En_Fossil(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.fossil.com/en-in/products/the-minimalist-three-hand-smoke-stainless-steel-watch/FS5459.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("In_En_Fossil", "pass"))
                except:
                    list1.append(("In_En_Fossil", "false"))

            def test_AWhatgoesaroundnyc(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.whatgoesaroundnyc.com/bags/shoulder-bags/louis-vuitton-monogram-canvas-boetie-mm-qjbahh5v0a082/QJBAHH5V0A082.html?lang=en_US')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("AWhatgoesaroundnyc", "pass"))
                except:
                    list1.append(("AWhatgoesaroundnyc", "false"))

            def test_En_Us_Mcmworldwide(self, driver, ):
                page_list = PageList(driver,
                                     'https://us.mcmworldwide.com/en_US/women/new-arrivals/reversible-liz-shopper-in-visetos/MWPDSLR02CO001.html?cgid=women-new-arrivals')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("En_Us_Mcmworldwide", "pass"))
                except:
                    list1.append(("En_Us_Mcmworldwide", "false"))

            def test_Tourneau(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.tourneau.com/watches/pre-owned-iwc/pilots-spitfire-chronograph-stainless-steel-automatic-iw371702-VIW02339.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Tourneau", "pass"))
                except:
                    list1.append(("Tourneau", "false"))

            def test_Hamilton_Jewelers(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.hamiltonjewelers.com/14k-yellow-gold-and-pink-enamel-huggie-hoops.html')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "action-close").click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_tangiblee_button()
                    list1.append(("Hamilton_Jewelers", "pass"))
                except:
                    list1.append(("Hamilton_Jewelers", "false"))

            def test_HeritageAuctions(self, driver, ):  # капча
                page_list = PageList(driver,
                                     'https://jewelry.ha.com/itm/estate-jewelry/rings/fancy-intense-yellow-diamond-diamond-platinum-gold-ring/a/5533-55336.s?ic=Home-FeaturedItems-071515')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("HeritageAuctions", "pass"))
                except:
                    list1.append(("HeritageAuctions", "false"))

            def test_De_At_MCMWorldwide(self, driver, ):
                page_list = PageList(driver,
                                     'https://at.mcmworldwide.com/de_AT/herren/taschen/g%C3%BCrteltaschen/fursten-g%C3%BCrteltasche-in-visetos/MMZAAFI04CO001.html?cgid=men-belt-bags')
                page_list.open()
                time.sleep(5)
                driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("co_th_samsonite", "pass"))
                except:
                    list1.append(("co_th_samsonite", "false"))

            def test_co_th_samsonite(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.samsonite.co.th/th/zalia-2/bailhandle-3-comp-14.1%22/ss-129439-1549.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("co_th_samsonite", "pass"))
                except:
                    list1.append(("co_th_samsonite", "false"))

            def test_Tw_Samsonite(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.samsonite.com.tw/samsonite/karissa-2/backpack-3pkt-1-buckle/ss-130799-1041.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Tw_Samsonite", "pass"))
                except:
                    list1.append(("Tw_Samsonite", "false"))

            def test_Sg_Samsonite(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.samsonite.com.sg/samsonite-red/aydin/cross/ss-137479-1694.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Sg_Samsonite", "pass"))
                except:
                    list1.append(("Sg_Samsonite", "false"))

            def test_My_Samsonite(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.samsonite.com.my/varsity/backpack-n3/ss-125216-1041.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("My_Samsonite", "pass"))
                except:
                    list1.append(("My_Samsonite", "false"))

            def test_Hk_AmericanTourister(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.americantourister.com.hk/zh/american-tourister/alizee-summer/backpack-1-as/at-140103-1041.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Hk_AmericanTourister", "pass"))
                except:
                    list1.append(("Hk_AmericanTourister", "false"))

            def test_Hk_En_Samsonite(self, driver, ):
                page_list = PageList(driver,
                                     'https://www.samsonite.com.hk/en/karissa/backpack-1-pocket-lb/ss-124048-8024.html')
                page_list.open()
                time.sleep(5)
                page_list.scroll()
                time.sleep(5)
                try:
                    page_list.find_cta()
                    list1.append(("Hk_En_Samsonite", "pass"))
                except:
                    list1.append(("Hk_En_Samsonite", "false"))
                page_list.write()
