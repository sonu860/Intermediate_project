import qrcode

class QRCode:

    def qr_generator(self):

        print("\n" + "="*40)
        print("   Welcome to Qr Code")
        print("\n" + "="*40)

        data = input("\n Enter the URL link ==> ")


        # customization options
        print("\nCustomization options:")
        print("1. Default (black & white)")
        print("2. Custom colors")
        color_choice = input("Choose (1 or 2): ")

        qr = qrcode.QRCode(
            version= 1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size= 10,
            border= 4,
        )

        qr.add_data(data)
        qr.make(fit=True)


        if color_choice == '2':
            fill = input("Fill color (e.g., blue, red, #FF0000): ")
            back = input("Background color (e.g., white, yellow): ")
        else:
            fill = 'black'
            back = 'White'

        img = qr.make_image(fill_color=fill,back_color=back)
        filename = 'my_qrcode.png'
        img.save(filename)


        print(f"\n✅ QR code saved as {filename}")
        print(f"📱 Scan karo aur dekho: {data}")
    

q = QRCode()
q.qr_generator()



    


