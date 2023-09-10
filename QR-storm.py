
        img, _, err := image.Decode(bytes.NewReader(buffer[:n]))
        if err != nil {
            fmt.Println("Ошибка при декодировании изображения:", err)
            continue
        }


        qrCodes, err := qrcode.DecodeAll(img)
        if err != nil {
            fmt.Println("Ошибка при считывании QR-кода:", err)
            continue
        }


        for _, qrCode := range qrCodes {
            fmt.Println("Содержимое QR-кода:", qrCode.Payload)
        }
    }
}