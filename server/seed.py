from app import app
from models import db, User, PriceRanges, GPU, CPU, Memory, MotherBoard, Storage, PSU, Case, BuildType, Builds, BuildComponents
import bcrypt

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        hashed_pw1 = bcrypt.hashpw('password1'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        hashed_pw2 = bcrypt.hashpw('password2'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        user1 = User(username='kyle', password=hashed_pw1)
        user2 = User(username='Bob', password=hashed_pw2)

        users = [user1, user2]
        db.session.add_all(users)

        # Add Price Ranges
        Price_range1 = PriceRanges(min_price=500, max_price=750)
        Price_range2 = PriceRanges(min_price=751, max_price=1000)
        Price_range3 = PriceRanges(min_price=1001, max_price=1500)
        Price_range4 = PriceRanges(min_price=1501, max_price=99999)

        Price_ranges = [Price_range1, Price_range2, Price_range3, Price_range4]
        db.session.add_all(Price_ranges)

        build_type1 = BuildType(type_name="Gaming")
        build_type2 = BuildType(type_name="Workstation")
        build_type3 = BuildType(type_name="Balanced")

        build_types = [build_type1, build_type2, build_type3]
        db.session.add_all(build_types)
        db.session.commit()

        #Seeding for GPUs
        gpu1 = GPU(name='MSI RTX 3060 VENTUS', Speed=1807, Price=289.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-137-632-03.jpg', purchase_link='https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-ventus-2x-12g-oc/p/N82E16814137632?Item=N82E16814137632')
        gpu2 = GPU(name='MSI Mech Radeon RX 6650 XT', Speed=2048, Price=249.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-137-737-01.jpg', purchase_link='https://www.newegg.com/msi-rx-6650-xt-mech-2x-8g-oc/p/N82E16814137737?Item=N82E16814137737')
        gpu3 = GPU(name='ASRock Radeon RX 6600', Speed=2491, Price=209.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-930-066-07.jpg', purchase_link='https://www.newegg.com/asrock-radeon-rx-6600-rx6600-cld-8g/p/N82E16814930066?Item=N82E16814930066')
        gpu4 = GPU(name='XFX SpeedSTER QICK308 RADEON RX 7600', Speed=2755, Price=269.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-150-880-09.jpg', purchase_link='https://www.newegg.com/xfx-radeon-rx-7600-rx-76pqickby/p/N82E16814150880?Item=N82E16814150880')
        gpu5 = GPU(name='ASUS Dual GeForce RTX 4060 OC Edition', Speed=3072, Price=299.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-126-665-02.png', purchase_link='https://www.newegg.com/asus-geforce-rtx-4060-dual-rtx4060-o8g/p/N82E16814126665?Item=N82E16814126665')
        gpu6 = GPU(name='MSI Ventus GeForce RTX 4060', Speed=3072, Price=299.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-137-804-11.jpg', purchase_link='https://www.newegg.com/msi-geforce-rtx-4060-rtx-4060-ventus-2x-black-8g-oc/p/N82E16814137804?Item=N82E16814137804')
        gpu7 = GPU(name='MSI Mech Radeon RX 7600', Speed=2695, Price=269.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-137-795-10.jpg', purchase_link='https://www.newegg.com/msi-radeon-rx-7600-rx-7600-mech-2x-classic-8g-oc/p/N82E16814137795?Item=N82E16814137795')
        gpu8 = GPU(name='SAPPHIRE PULSE Radeon RX 6400', Speed=2321, Price=143.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-202-416-01.jpg', purchase_link='https://www.newegg.com/sapphire-radeon-rx-6400-11315-01-20g/p/N82E16814202416?Item=N82E16814202416')
        gpu9 = GPU(name='MSI Ventus GeForce GTX 1650', Speed=1620, Price=151.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-137-593-S06.jpg', purchase_link='https://www.newegg.com/msi-geforce-gtx-1650-gtx-1650-d6-ventus-xs-ocv1/p/N82E16814137593?Item=N82E16814137593')
        gpu10 = GPU(name='EVGA GeForce RTX 2060 SC GAMING', Speed=1710, Price=219.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-487-434-V06.jpg', purchase_link='https://www.newegg.com/evga-geforce-rtx-2060-06g-p4-2062-kr/p/N82E16814487434?Item=N82E16814487434')
        gpu11 = GPU(name='ASRock Radeon RX 6700 XT Challenger', Speed=2581, Price=329.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-930-056-01.jpg', purchase_link='https://www.newegg.com/asrock-radeon-rx-6700-xt-rx6700xt-cld-12g/p/N82E16814930056')
        gpu12 = GPU(name='ASRock Challenger Pro Radeon RX 6750 XT', Speed=2618, Price=359.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-930-071-02.jpg', purchase_link='https://www.newegg.com/asrock-radeon-rx-6750-xt-rx6750xt-clp-12go/p/N82E16814930071')
        gpu13 = GPU(name='ZOTAC GAMING GeForce RTX 3070 Ti', Speed=1770, Price=449.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-500-547-09.jpg', purchase_link='https://www.newegg.com/zotac-geforce-rtx-3070-ti-zt-a30710q-10p/p/N82E16814500547')
        gpu14 = GPU(name='PowerColor Fighter AMD Radeon RX 6800', Speed=2105, Price=439.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-131-771-02.jpg', purchase_link='https://www.newegg.com/powercolor-radeon-rx-6800-axrx-6800-16gbd6-3dh-oc/p/N82E16814131771')
        gpu15 = GPU(name='SAPPHIRE PULSE Radeon RX 7700 XT', Speed=2544, Price=449.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-202-436-11.jpg', purchase_link='https://www.newegg.com/sapphire-radeon-rx-7700-xt-11335-04-20g/p/N82E16814202436')
        gpu16 = GPU(name='GIGABYTE GeForce RTX 4060 Ti EAGLE', Speed=2535, Price=399.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-932-620-10.jpg', purchase_link='https://www.newegg.com/gigabyte-geforce-rtx-4060-ti-gv-n406teagle-8gd/p/N82E16814932620')
        gpu17 = GPU(name='XFX SpeedSTER SWFT309 AMD Radeon RX 6700 XT', Speed=2581, Price=339.99, ProductImage='https://c1.neweggimages.com/ProductImage/14-150-852-V08.jpg', purchase_link='https://www.newegg.com/xfx-radeon-rx-6700-xt-rx-67xtyjfdv/p/N82E16814150852')
        gpu18 = GPU(name='MSI Gaming Radeon RX 6750 XT', Speed=2623, Price=384.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-137-734-V01.jpg', purchase_link='https://www.newegg.com/msi-rx-6750-xt-gaming-x-trio-12g/p/N82E16814137734')
        gpu19 = GPU(name='ASUS Dual GeForce RTX 4060 Ti', Speed=2580, Price=449.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-126-678-01.png', purchase_link='https://www.newegg.com/asus-geforce-rtx-4060-ti-dual-rtx4060ti-a16g/p/N82E16814126678')
        gpu20 = GPU(name='XFX SpeedSTER QICK319 Radeon RX 7700 XT', Speed=2599, Price=459.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-150-884-06.jpg', purchase_link='https://www.newegg.com/xfx-radeon-rx-7700-xt-rx-77tqickb9/p/N82E16814150884')
        gpu21 = GPU(name='XFX Speedster MERC 319 AMD RX 6950 XT', Speed=2368, Price=629.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/27N-0002-00172-12.jpg', purchase_link='https://www.newegg.com/xfx-radeon-rx-6950-xt-rx-695xatbd9/p/27N-0002-00172')
        gpu22 = GPU(name='XFX SpeedSTER MERC310 Radeon RX 7900 XTX', Speed=2615, Price=969.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-150-878-16.jpg', purchase_link='https://www.newegg.com/xfx-radeon-rx-7900-xtx-rx-79xmercb9/p/N82E16814150878')
        gpu23 = GPU(name='MSI Gaming GeForce RTX 4070 Ti', Speed=2745, Price=849.00, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-137-771-02.jpg', purchase_link='https://www.newegg.com/msi-geforce-rtx-4070-ti-rtx-4070-ti-gaming-x-trio-12g/p/N82E16814137771')
        gpu24 = GPU(name='MSI Gaming GeForce RTX 4080', Speed=2580, Price=1269.99, ProductImage='https://c1.neweggimages.com/ProductImage/14-137-766-01.jpg', purchase_link='https://www.newegg.com/msi-geforce-rtx-4080-rtx-4080-16gb-gaming-x-trio/p/N82E16814137766')
        gpu25 = GPU(name='GIGABYTE GeForce RTX 4090 WINDFORCE V2', Speed=2520, Price=1659.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/14-932-632-23.jpg', purchase_link='https://www.newegg.com/gigabyte-geforce-rtx-4090-gv-n4090wf3v2-24gd/p/N82E16814932625')
        
        all_gpus = [gpu1, gpu2, gpu3, gpu4, gpu5, gpu6, gpu7, gpu8, gpu9, gpu10, 
            gpu11, gpu12, gpu13, gpu14, gpu15, gpu16, gpu17, gpu18, gpu19, 
            gpu20, gpu21, gpu22, gpu23, gpu24, gpu25]
        db.session.add_all(all_gpus)

        #seeding for CPUs
        cpu1 = CPU(name='AMD Ryzen 7 7800X3D', type='AMD AM5', Speed=5.0, Price=399.00, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/19-113-793-03.png', purchase_link='https://www.newegg.com/amd-ryzen-7-7800x3d-ryzen-7-7000-series/p/N82E16819113793')
        cpu2 = CPU(name='AMD Ryzen 5 5600X', type='AMD AM4', Speed=4.6, Price=175.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/19-113-666-V01.jpg', purchase_link='https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666')
        cpu3 = CPU(name='AMD Ryzen 7 5800X', type='AMD AM4', Speed=4.7, Price=249.00, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/19-113-665-V01.jpg', purchase_link='https://www.newegg.com/amd-ryzen-7-5800x/p/N82E16819113665')
        cpu4 = CPU(name='AMD Ryzen 7 5800X3D', type='AMD AM4', Speed=4.5, Price=346.00, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/19-113-734-S04.jpg', purchase_link='https://www.newegg.com/amd-ryzen-7-5800x3d-ryzen-7-5000-series/p/N82E16819113734')
        cpu5 = CPU(name='AMD Ryzen 9 7950X3D', type='AMD AM5', Speed=5.7, Price=684.00, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/19-113-791-03.png', purchase_link='https://www.newegg.com/amd-ryzen-9-7950x3d-ryzen-9-7000-series/p/N82E16819113791')
        cpu6 = CPU(name='AMD Ryzen 5 4500', type='AMD AM4', Speed=4.1, Price=77.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/ARUXS2204210J7PZ0CA.jpg', purchase_link='https://www.newegg.com/amd-ryzen-5-4500-ryzen-5-4000/p/N82E16819113738')
        cpu7 = CPU(name='Intel Core i7-12700K', type='Intel LGA 1700', Speed=3.6, Price=314.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/19-118-343-05.jpg', purchase_link='https://www.newegg.com/intel-core-i7-12700k-core-i7-12th-gen/p/N82E16819118343')
        cpu8 = CPU(name='Intel Core i7-13700K', type='Intel LGA 1700', Speed=3.4, Price=410.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/19-118-414-V01.jpg', purchase_link='https://www.newegg.com/intel-core-i7-13700k-core-i7-13th-gen/p/N82E16819118414')
        cpu9 = CPU(name='Intel Core i5-12600K', type='Intel LGA 1700', Speed=3.7, Price=247.49, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/19-118-347-05.jpg', purchase_link='https://www.newegg.com/intel-core-i5-12600k-core-i5-12th-gen/p/N82E16819118347')
        cpu10 = CPU(name='Intel Core i9-13900K', type='Intel LGA 1700', Speed=5.4, Price=569.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/19-118-412-V01.jpg', purchase_link='https://www.newegg.com/intel-core-i9-13900k-core-i9-13th-gen/p/N82E16819118412')
        cpu11 = CPU(name='Intel Core i5-12400F', type='Intel LGA 1700', Speed=4.4, Price=149.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/19-118-360-08.jpg', purchase_link='https://www.newegg.com/intel-core-i5-12400f-core-i5-12th-gen/p/N82E16819118360')
        cpu12 = CPU(name='Intel Core i3-12100', type='Intel LGA 1700', Speed=3.3, Price=118.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/A24GD2203220DB6YE7D.jpg', purchase_link='https://www.newegg.com/intel-core-i3-12100-core-i3-12th-gen/p/N82E16819118370')

        all_cpus = [cpu1, cpu2, cpu3, cpu4, cpu5, cpu6, cpu7, cpu8, cpu9, cpu10, cpu11, cpu12]
        db.session.add_all(all_cpus)

        #seeding for memory
        memory1 = Memory(name='G.SKILL Ripjaws V Series 32GB', Speed=3200, Size=32, Price=59.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-232-091-08.jpg', purchase_link='https://www.newegg.com/g-skill-32gb-288-pin-ddr4-sdram/p/N82E16820232091')
        memory2 = Memory(name='CORSAIR Vengeance 32GB DDR5', Speed=5600, Size=32, Price=94.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-236-828-V01.jpg', purchase_link='https://www.newegg.com/corsair-32gb-288-pin-ddr5-sdram/p/N82E16820236828')
        memory3 = Memory(name='G.SKILL Ripjaws V Series 16GB', Speed=3200, Size=16, Price=35.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-231-941-03.jpg', purchase_link='https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941')
        memory4 = Memory(name='CORSAIR Vengeance RGB Pro 32GB', Speed=3600, Size=32, Price=79.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-236-607-02.jpg', purchase_link='https://www.newegg.com/corsair-32gb-288-pin-ddr4-sdram/p/N82E16820236607')
        memory5 = Memory(name='G.SKILL Trident Z5 RGB Series 64GB DDR5', Speed=6400, Size=64, Price=209.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-374-432-07.png', purchase_link='https://www.newegg.com/g-skill-64gb/p/N82E16820374432')
        memory6 = Memory(name='CORSAIR Vengeance LPX 32GB', Speed=3600, Size=32, Price=69.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-236-596-S02.jpg', purchase_link='https://www.newegg.com/corsair-32gb-288-pin-ddr4-sdram/p/N82E16820236596')
        memory7 = Memory(name='CORSAIR Vengeance LPX 16GB', Speed=3200, Size=16, Price=39.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-233-859-01.jpg', purchase_link='https://www.newegg.com/corsair-16gb-288-pin-ddr4-sdram/p/N82E16820233859')
        memory8 = Memory(name='CORSAIR Vengeance 64GB', Speed=5200, Size=64, Price=159.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-236-839-V01.jpg', purchase_link='https://www.newegg.com/corsair-64gb-288-pin-ddr5-sdram/p/N82E16820236839')
        memory9 = Memory(name='G.SKILL Flare X5 Series AMD EXPO 32GB DDR5', Speed=6000, Size=32, Price=92.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-374-419-07.png', purchase_link='https://www.newegg.com/g-skill-32gb/p/N82E16820374419')
        memory10 = Memory(name='G.SKILL Trident Z RGB (For AMD) 16GB', Speed=3600, Size=16, Price=52.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-232-728-V01.jpg', purchase_link='https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820232728')
        memory11 = Memory(name='G.SKILL Trident Z RGB (For AMD) 32GB', Speed=3200, Size=32, Price=71.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-232-752-01.jpg', purchase_link='https://www.newegg.com/g-skill-32gb-288-pin-ddr4-sdram/p/N82E16820232752')
        memory12 = Memory(name='CORSAIR Vengeance LPX 64GB', Speed=3200, Size=64, Price=119.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-236-586-V01.jpg', purchase_link='https://www.newegg.com/corsair-64gb-288-pin-ddr4-sdram/p/N82E16820236586')
        memory13 = Memory(name='G.SKILL Trident Z Neo (For AMD Ryzen) Series 32GB', Speed=3600, Size=32, Price=94.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-232-861-V01.jpg', purchase_link='https://www.newegg.com/g-skill-32gb-288-pin-ddr4-sdram/p/N82E16820232861')
        memory14 = Memory(name='CORSAIR Vengeance RGB 32GB DDR5', Speed=6000, Size=32, Price=104.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-236-888-01.jpg', purchase_link='https://www.newegg.com/corsair-32gb/p/N82E16820236879')
        memory15 = Memory(name='G.SKILL Trident Z Royal Series 64GB', Speed=3600, Size=64, Price=640.61, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/20-374-204-V04.jpg', purchase_link='https://www.newegg.com/g-skill-64gb-288-pin-ddr4-sdram/p/N82E16820374204?Item=9SIA4YUJ954758')

        all_memory = [memory1, memory2, memory3, memory4, memory5, memory6, memory7, memory8, memory9, memory10, memory11, memory12, memory13, memory14, memory15]
        db.session.add_all(all_memory)

        motherBoard1 = MotherBoard(name= 'GIGABYTE B550M', Type= 'AM4', Price=109.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-145-250-V01.jpg', purchase_link='https://www.newegg.com/gigabyte-b550m-ds3h-ac/p/N82E16813145250')
        motherBoard2 = MotherBoard(name= 'ASRock B650E Taichi Lite AM5', Type= 'AM5', Price=279.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-162-135-05.png', purchase_link='https://www.newegg.com/asrock-b650e-taichi-lite/p/N82E16813162135')
        motherBoard3 = MotherBoard(name= 'ASRock B650M Pro RS WiFi', Type= 'AM5', Price=149.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-162-131-04.png', purchase_link='https://www.newegg.com/asrock-b650m-pro-rs/p/N82E16813162131')
        motherBoard4 = MotherBoard(name= 'MSI MAG X670E TOMAHAWK WIFI', Type= 'AM5', Price=299.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-144-595-06.png', purchase_link='https://www.newegg.com/msi-mag-x670e-tomahawk-wifi/p/N82E16813144595')
        motherBoard5 = MotherBoard(name= 'ASRock B550M PRO4', Type= 'AM4', Price=104.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-157-939-V01.jpg', purchase_link='https://www.newegg.com/asrock-b550m-pro4/p/N82E16813157939')
        motherBoard6 = MotherBoard(name= 'ASRock B550M Phantom Gaming 4', Type= 'AM4', Price=84.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-157-966-V05.jpg', purchase_link='https://www.newegg.com/asrock-b550m-phantom-gaming-4/p/N82E16813157966')
        motherBoard7 = MotherBoard(name= 'ASUS ROG STRIX X670E-E GAMING WIFI 6E', Type= 'AM5', Price=479.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-119-581-09.jpg', purchase_link='https://www.newegg.com/asus-rog-strix-x670e-e-gaming-wifi/p/N82E16813119581')
        motherBoard8 = MotherBoard(name= 'ASRock X670E Steel Legend', Type= 'AM5', Price=299.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-162-070-04.png', purchase_link='https://www.newegg.com/asrock-x670e-steel-legend/p/N82E16813162070')
        motherBoard9 = MotherBoard(name= 'MSI PRO Z790 GAMING PRO WIFI', Type= 'LGA 1700', Price=229.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-144-629-05.png', purchase_link='https://www.newegg.com/msi-z790-gaming-pro-wifi/p/N82E16813144629')
        motherBoard10 = MotherBoard(name= 'ASUS ROG STRIX Z790-H Gaming (WiFi 6E)', Type= 'LGA 1700', Price=279.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-119-635-02.png', purchase_link='https://www.newegg.com/p/N82E16813119635')
        motherBoard11 = MotherBoard(name= 'EVGA Z790 CLASSIFIED', Type= 'LGA 1700', Price=489.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-188-206-01.jpg', purchase_link='https://www.newegg.com/p/N82E16813188206')
        motherBoard12 = MotherBoard(name= 'GIGABYTE B760M AORUS ELITE AX', Type= 'LGA 1700', Price=169.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-145-422-01.jpg', purchase_link='https://www.newegg.com/p/N82E16813145422')
        motherBoard13 = MotherBoard(name= 'ASUS TUF Gaming Z690-Plus WiFi', Type= 'LGA 1700', Price=159.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-119-554-V01.jpg', purchase_link='https://www.newegg.com/asus-tuf-gaming-z690-plus-wifi/p/N82E16813119554')
        motherBoard14 = MotherBoard(name= 'ASUS ROG Maximus Z690 Hero(WiFi 6E)', Type= 'LGA 1700', Price=349.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-119-504-V07.jpg', purchase_link='https://www.newegg.com/asus-rog-maximus-z690-hero/p/N82E16813119504')
        motherBoard15 = MotherBoard(name= 'ASRock B660M PRO RS', Type= 'LGA 1700', Price=99.99, ProductImage='https://c1.neweggimages.com/ProductImageCompressAll1280/13-162-048-V01.jpg', purchase_link='https://www.newegg.com/p/N82E16813162048')

        all_mother_boards = [motherBoard1, motherBoard2, motherBoard3, motherBoard4, motherBoard5, motherBoard6, motherBoard7, motherBoard8, motherBoard9, motherBoard10, motherBoard11, motherBoard12, motherBoard13, motherBoard14, motherBoard15]
        db.session.add_all(all_mother_boards)

        storage1 = Storage(name= 'Seagate BarraCuda', type= 'hdd', Size=4, Price=74.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/22-179-299-V01.jpg', purchase_link= 'https://www.newegg.com/seagate-barracuda-st4000dm004-4tb/p/N82E16822179299?Item=N82E16822179299')
        storage2 = Storage(name= 'Seagate BarraCuda', type= 'hdd', Size=8, Price=119.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/22-183-793-V06.jpg', purchase_link= 'https://www.newegg.com/seagate-barracuda-st8000dm004-8tb/p/N82E16822183793?Item=N82E16822183793')
        storage3 = Storage(name= 'Seagate BarraCuda', type= 'hdd', Size=1, Price=53.49, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/22-179-010-V02.jpg', purchase_link= 'https://www.newegg.com/seagate-barracuda-st1000dm010-1tb/p/N82E16822179010?Item=N82E16822179010')
        storage4 = Storage(name= 'Seagate Exos X20', type= 'hdd', Size=20, Price=279.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/22-185-011-01.jpg', purchase_link= 'https://www.newegg.com/seagate-exos-x20-st20000nm007d-20tb/p/N82E16822185011?Item=N82E16822185011')
        storage5 = Storage(name= 'WD_BLACK SN850X', type= 'NVMe M.2 2280', Size=2, Price=119.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-250-247-02.jpg', purchase_link= 'https://www.newegg.com/western-digital-2tb-black-sn850x-nvme/p/N82E16820250247?Item=N82E16820250247&SoldByNewegg=1')
        storage6 = Storage(name= 'SAMSUNG 990 PRO', type= 'NVME M.2 2280', Size=2, Price=169.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-147-861-01.jpg', purchase_link= 'https://www.newegg.com/samsung-2tb-990-pro/p/N82E16820147861?Item=N82E16820147861&SoldByNewegg=1')
        storage7 = Storage(name= 'Solidigm P41 Plus', type= 'NVME M.2 2280', Size=2, Price=64.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-329-022-16.png', purchase_link= 'https://www.newegg.com/solidigm-2tb-p41-plus/p/N82E16820329022?Item=N82E16820329022&SoldByNewegg=1')
        storage8 = Storage(name= 'SAMSUNG 990 PRO', type= 'NVME M.2 2280', Size=1, Price=99.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-147-860-01.jpg', purchase_link= 'https://www.newegg.com/samsung-1tb-990-pro/p/N82E16820147860?Item=N82E16820147860&SoldByNewegg=1')
        storage9 = Storage(name= 'Western Digital WD_BLACK SN770', type= 'NVME M.2 2280', Size=1, Price=50.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-250-217-V05.jpg', purchase_link= 'https://www.newegg.com/western-digital-1tb-sn770/p/N82E16820250217?Item=N82E16820250217&SoldByNewegg=1')
        storage10 = Storage(name= 'Crucial MX500', type= 'SSD', Size=1, Price=47.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-156-174-V09.jpg', purchase_link= 'https://www.newegg.com/crucial-mx500-1tb/p/N82E16820156174?Item=N82E16820156174&SoldByNewegg=1')
        storage11 = Storage(name= 'SAMSUNG 870 EVO Series', type= 'SSD', Size=1, Price=59.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-147-793-V07.jpg', purchase_link= 'https://www.newegg.com/samsung-1tb-870-evo-series/p/N82E16820147793?Item=N82E16820147793&SoldByNewegg=1')
        storage12 = Storage(name= 'SAMSUNG 870 EVO Series', type= 'SSD', Size=2, Price=129.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-147-794-V01.jpg', purchase_link= 'https://www.newegg.com/samsung-2tb-870-evo-series/p/N82E16820147794?Item=N82E16820147794&SoldByNewegg=1')
        storage13 = Storage(name= 'SAMSUNG 870 QVO Series', type= 'SDD', Size=8, Price=399.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-147-784-V01.jpg', purchase_link= 'https://www.newegg.com/samsung-8tb-870-qvo-series/p/N82E16820147784?Item=N82E16820147784&SoldByNewegg=1')
        storage14 = Storage(name= 'SAMSUNG T7 Portable', type= 'External SSD', Size=2, Price=129.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-147-768-V01.jpg', purchase_link= 'https://www.newegg.com/samsung-t7-2tb/p/N82E16820147768?Item=N82E16820147768&SoldByNewegg=1')
        storage15 = Storage(name= 'SanDisk Extreme PRO V2', type= 'External SSD', Size=4, Price=299.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/20-173-501-V01.jpg', purchase_link= 'https://www.newegg.com/sandisk-extreme-pro-v2-4tb/p/N82E16820173501?Item=N82E16820173501&SoldByNewegg=1')

        all_storage = [storage1, storage2, storage3, storage4, storage5, storage6, storage7, storage8, storage9, storage10, storage11, storage12, storage13, storage14, storage15]
        db.session.add_all(all_storage)

        psu1 = PSU(name= 'CORSAIR RM850e Fully Modular Low-Noise', Wattage=850, Price=129.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/17-139-301-08.png', purchase_link= 'https://www.newegg.com/corsair-rm850e-cp-9020263-na-850-w/p/N82E16817139306?Item=N82E16817139306')
        psu2 = PSU(name= 'Segotep 750W Power Supply Full Modular', Wattage=750, Price=89.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/AM7KS2212200KJIB0C1.jpg', purchase_link= 'https://www.newegg.com/segotep-gp-series-750w-fully-modular/p/1HU-00Z0-00006?Item=9SIBGX1JA26866&cm_sp=SP-_-1594522-_-Pers_CategorySponsoredProduct-_-4-_-9SIBGX1JA26866-_-32-_--_-3')
        psu3 = PSU(name= 'be quiet! PURE POWER 12 M 1200W 80+ Gold', Wattage=1200, Price=199.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/A68VS2306080ZMG2ED1.jpg', purchase_link= 'https://www.newegg.com/p/1HU-004H-000S9?Item=9SIA68VJYG8004')
        psu4 = PSU(name= 'FSP Hydro PTM X PRO 1000W, ATX 3.0 & PCIe 5.0(Gen 5), 80+ Platinum', Wattage=1000, Price=279.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/ABP9S23020617QFV488.jpg', purchase_link= 'https://www.newegg.com/p/1HU-0095-000Y6?Item=9SIABP9JJV7176&cm_sp=SP-_-2082509-_-Pers_CategorySponsoredProduct-_-4-_-9SIABP9JJV7176-_-32-_--_-9')
        psu5 = PSU(name= 'ASUS TUF Gaming 1000W Gold', Wattage=1000, Price=159.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/17-320-029-06.png', purchase_link= 'https://www.newegg.com/asus-tuf-gaming-1000g-1000-w/p/N82E16817320029?Item=N82E16817320029')
        psu6 = PSU(name= 'be quiet! Dark Power 13 - 1000W 80 PLUS Titanium', Wattage=1000, Price=289.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/A68VS2301270XTEZS9A.jpg', purchase_link= 'https://www.newegg.com/p/1HU-004H-000R8?Item=9SIA68VJJ74129')
        psu7 = PSU(name= 'Rosewill CMG1000G5 PCIE 5.0, 80 GOLD', Wattage=1000, Price=109.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/17-182-453-01.jpg', purchase_link= 'https://www.newegg.com/rosewill-cmg1000g5-1000-w/p/N82E16817182453?Item=N82E16817182453')
        psu8 = PSU(name= 'Thermaltake Toughpower GX2 80+ Gold', Wattage=600, Price=66.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/17-153-415-V10.jpg', purchase_link= 'https://www.newegg.com/thermaltake-toughpower-gx2-gold-ps-tpd-0600nnfagu-2-600w/p/N82E16817153415?Item=N82E16817153415')
        psu9 = PSU(name= 'Rosewill SMG Series, SMG850, 850W Fully Modular Power Supply, 80 PLUS GOLD', Wattage=850, Price=85.00, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/17-182-443-V81.jpg', purchase_link= 'https://www.newegg.com/rosewill-smg-series-smg850-850w/p/N82E16817182443?Item=N82E16817182443')
        psu10 = PSU(name= 'CORSAIR HX850 Fully Modular Ultra-Low Noise', Wattage=850, Price=134.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/17-139-311-01.png', purchase_link= 'https://www.newegg.com/corsair-hx-series-hx850-850-w/p/N82E16817139311?Item=N82E16817139311')
        
        all_psu = [psu1, psu2, psu3, psu4, psu5, psu6, psu7, psu8, psu9, psu10]
        db.session.add_all(all_psu)

        case1 = Case(name= 'Corsair 4000D Airflow', Type= 'ATX Mid', Price=94.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-139-156-V01.jpg', purchase_link= 'https://www.newegg.com/black-corsair-4000d-airflow-atx-mid-tower/p/N82E16811139156')
        case2 = Case(name= 'Fractal Design North', Type= 'ATX Mid', Price=139.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-352-204-21.jpg', purchase_link= 'https://www.newegg.com/p/N82E16811352204')
        case3 = Case(name= 'LIAN LI O11 Dynamic EVO', Type= 'ATX Mid', Price=153.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/AFSTS211210aAqTM.jpg', purchase_link= 'https://www.newegg.com/black-lian-li-o11-dynamic-evo-atx-mid-tower/p/2AM-000Z-00093')
        case4 = Case(name= 'Fractal Design Terra Jade', Type= 'Mini ITX', Price=179.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-352-214-21.jpg', purchase_link= 'https://www.newegg.com/jade-fractal-design-terra-small-form-factor/p/N82E16811352214')
        case5 = Case(name= 'DeepCool CC560', Type= 'ATX Mid', Price=59.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-853-125-01.jpg', purchase_link= 'https://www.newegg.com/p/N82E16811853125')
        case6 = Case(name= 'Fractal Design Torrent Black', Type= 'ATX Mid', Price=189.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-352-143-01.jpg', purchase_link= 'https://www.newegg.com/black-fractal-design-torrent-atx-mid-tower/p/N82E16811352143')
        case7 = Case(name= 'Fractal Design Focus G', Type= 'ATX Mid', Price=54.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-352-069-V16.jpg', purchase_link= 'https://www.newegg.com/black-fractal-design-focus-g-atx-mid-tower/p/N82E16811352069')
        case8 = Case(name= 'DIYPC ARGB-Q3-BK Black USB3.0 Tempered Glass', Type= 'Micro ATX', Price=68.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-353-224-13.jpg', purchase_link= 'https://www.newegg.com/p/N82E16811353224')
        case9 = Case(name= 'HYTE Y60 Modern Aesthetic Dual Chamber Panoramic Tempered Glass', Type= 'ATX Mid', Price=189.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-737-002-16.jpg', purchase_link= 'https://www.newegg.com/black-hyte-y60-atx-mid-tower/p/N82E16811737002')
        case10 = Case(name= 'NZXT H9 Flow', Type= 'ATX Mid', Price=159.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-146-347-10.png', purchase_link= 'https://www.newegg.com/nzxt-h9-flow-all-black-atx-mid-tower/p/N82E16811146347')
        case11 = Case(name= 'Thermaltake Versa H17', Type= 'Micro ATX', Price=39.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-133-364-V01.jpg', purchase_link= 'https://www.newegg.com/black-thermaltake-versa-h17-micro-gaming-chassis/p/N82E16811133364')
        case12 = Case(name= 'ASUS AP201 Type-C Airflow-focused', Type= 'Micro ATX', Price=79.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/A4RES22061007RXFU34.jpg', purchase_link= 'https://www.newegg.com/black-asus-prime-micro-atx-tower/p/2AM-0033-000F0')
        case13 = Case(name= 'Phanteks Enthoo Pro Series', Type= 'ATX Full', Price=139.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-854-003-01.jpg', purchase_link= 'https://www.newegg.com/black-phanteks-enthoo-pro-atx-full-tower/p/N82E16811854003')
        case14 = Case(name= 'Phanteks NV7', Type= 'ATX Full', Price=219.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-854-123-01.jpg', purchase_link= 'https://www.newegg.com/white-phanteks-nv7-series-atx-full-tower/p/N82E16811854123')
        case15 = Case(name= 'Phanteks Evolv Shift 2', Type= 'Mini ITX', Price=89.99, ProductImage= 'https://c1.neweggimages.com/ProductImageCompressAll1280/11-854-107-V09.jpg', purchase_link= 'https://www.newegg.com/anthracite-grey-phanteks-evolv-shift-2-mini-itx-tower/p/N82E16811854107')

        all_cases = [case1, case2, case3, case4, case5, case6, case7, case8, case9, case10, case11, case12, case13, case14, case15]
        db.session.add_all(all_cases)

        build1 = Builds(price_range_id=Price_range1.id, build_type_id=build_type1.id)
        build2 = Builds(price_range_id=Price_range1.id, build_type_id=build_type2.id)
        build3 = Builds(price_range_id=Price_range1.id, build_type_id=build_type3.id)
        build4 = Builds(price_range_id=Price_range2.id, build_type_id=build_type1.id)
        build5 = Builds(price_range_id=Price_range2.id, build_type_id=build_type2.id)
        build6 = Builds(price_range_id=Price_range2.id, build_type_id=build_type3.id)
        build7 = Builds(price_range_id=Price_range3.id, build_type_id=build_type1.id)
        build8 = Builds(price_range_id=Price_range3.id, build_type_id=build_type2.id)
        build9 = Builds(price_range_id=Price_range3.id, build_type_id=build_type3.id)

        all_builds = [build1, build2, build3, build4, build5, build6, build7, build8, build9]
        db.session.add_all(all_builds)
        db.session.commit()

        build1_components = BuildComponents(
        build_id=build1.id,
        gpu_id=9,  
        cpu_id=6,
        case_id=7,
        memory_id=3,
        motherboard_id=6,
        psu_id=8,
        storage_id=7
        )
        db.session.add(build1_components)

        build2_components = BuildComponents(
        build_id=build2.id,
        gpu_id=8,  
        cpu_id=2,
        case_id=7,
        memory_id=3,
        motherboard_id=6,
        psu_id=8,
        storage_id=7
        )
        db.session.add(build2_components)

        build3_components = BuildComponents(
        build_id=build3.id,
        gpu_id=9,  
        cpu_id=12,
        case_id=7,
        memory_id=3,
        motherboard_id=15,
        psu_id=8,
        storage_id=7
        )
        db.session.add(build3_components)

        build4_components = BuildComponents(
        build_id=build4.id,
        gpu_id=1,  
        cpu_id=12,
        case_id=7,
        memory_id=3,
        motherboard_id=15,
        psu_id=8,
        storage_id=5
        )
        db.session.add(build4_components)

        build5_components = BuildComponents(
        build_id=build5.id,
        gpu_id=10,  
        cpu_id=9,
        case_id=7,
        memory_id=3,
        motherboard_id=13,
        psu_id=8,
        storage_id=5
        )
        db.session.add(build5_components)

        build6_components = BuildComponents(
        build_id=build6.id,
        gpu_id=2,  
        cpu_id=11,
        case_id=7,
        memory_id=3,
        motherboard_id=15,
        psu_id=8,
        storage_id=5
        )
        db.session.add(build6_components)

        build7_components = BuildComponents(
        build_id=build7.id,
        gpu_id=21,  
        cpu_id=4,
        case_id=5,
        memory_id=4,
        motherboard_id=3,
        psu_id=1,
        storage_id=12
        )
        db.session.add(build7_components)

        build8_components = BuildComponents(
        build_id=build8.id,
        gpu_id=20,  
        cpu_id=5,
        case_id=5,
        memory_id=4,
        motherboard_id=2,
        psu_id=1,
        storage_id=12
        )
        db.session.add(build8_components)

        build9_components = BuildComponents(
        build_id=build9.id,
        gpu_id=20,  
        cpu_id=4,
        case_id=5,
        memory_id=4,
        motherboard_id=3,
        psu_id=1,
        storage_id=12
        )
        db.session.add(build9_components)


        db.session.commit()


