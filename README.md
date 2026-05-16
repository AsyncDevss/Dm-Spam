# ⚡ Çoklu Token DM Bot Sistemi 

Bu proje, belirlenen bir hedef kullanıcıya (User ID) birden fazla bot hesabı (token) üzerinden eş zamanlı ve sürekli olarak DM (Direkt Mesaj) göndermek amacıyla tasarlanmış gelişmiş bir Discord bot altyapısıdır. 

Sistem, **1 Ana Bot** ve **15 Yardımcı Bot** mantığıyla çalışır. Sunucudaki komut çakışmalarını ve mesaj kirliliğini önlemek adına sadece Ana Bot komutları dinler ve yanıtlar; yardımcı botlar ise sadece arka planda hedefi asenkron olarak döngüye alır.

---

## ✨ Özellikler

*   **⚡ 16 Bot Desteği:** Tek bir komutla 16 botun tamamı aynı anda harekete geçer.
*   **🧩 Komut Çakışması Engeli:** Sunucuda sadece ilk sıradaki **Ana Bot** komutlara tepki verir, diğer botlar sohbete yazıp kirlilik yaratmaz.
*   **🛑 Gelişmiş Durdurma:** `.stop` komutu verildiği an tüm botların döngüsü eş zamanlı olarak kesilir.
*   **🛡️ Hız Sınırı (Rate Limit) Koruması:** Botların Discord API'sinden ban yememesi veya hesapların kapanmaması için akıllı asenkron bekleme süreleri ve `HTTP 429` kontrolü entegre edilmiştir.
*   **🎨 Cyberpunk Estetiği:** Şık tasarlanmış modern, pembe/mavi tonlarında gömülü (Embed) yardım menüsü.

---

## 🛠️ Kurulum ve Çalıştırma

### 1. Gereksinimleri Yükleyin
Sistemin çalışması için Python ortamınızda `discord.py` kütüphanesinin kurulu olması gerekir:
```bash
pip install discord.py
