
# Cenker_llma_UI

Bu proje, **Python** ve **[Ollama](https://github.com/jmorganca/ollama)** kullanarak yerel bir (offline) Llama modeliyle sohbet edebilmenizi sağlayan basit bir **Tkinter** arayüz uygulamasıdır. 

## Özellikler

- **Yerel Model Entegrasyonu**: Ollama sayesinde, sunucu tarafında API ihtiyacı olmaksızın kendi makinenizde Llama modelini çalıştırabilirsiniz.  
- **Basit Arayüz**: Tkinter ile hızlıca masaüstü benzeri bir sohbet ekranı oluşturulur.  
- **Sohbet Bağlamı**: Kullanıcı mesajları ve Asistan yanıtları, kod içerisinde “conversation_history” olarak tutulur. Böylece önceki mesajları yeniden prompt’a ekleyerek **bağlamı korumaya** yardımcı olur.  
- **Esnek Prompt**: Prompt’u istediğiniz gibi özelleştirebilir, model ayarlarını (temperature, top_p vb.) `generate()` çağrısında değiştirebilirsiniz.

## Kurulum 

1. **Python 3.9+**  
   - macOS’ta veya diğer işletim sistemlerinde (Windows/Linux) en az Python 3.9 önerilir.  
   - Mevcut Python sürümünüzü kontrol etmek için:  
     ```bash
     python3 --version
     ```

2. **[Ollama](https://github.com/jmorganca/ollama)**  
   - Ollama, Llama ve benzeri modelleri yerelde çalıştırmayı sağlayan bir araçtır.  
   - macOS için Homebrew üzerinden yükleme:
     ```bash
     brew install --cask ollama
     ```
   - Yükledikten sonra sürümü kontrol edebilirsiniz:
     ```bash
     ollama version
     ```

3. **`ollama-python` Paketi**  
   - Bu Python paketi, Ollama ile Python arasında bir arayüz sunar. Kurmak için:
     ```bash
     pip install ollama
     ```
   - (Alternatif olarak `pip install git+https://github.com/ollama/ollama-python.git` gibi bir komutla en güncel sürüm elde edebilirsiniz.)

4. **Diğer Python Kütüphaneleri**  
   - `tkinter` (standart Python kütüphanesiyle çoğunlukla birlikte gelir)  
   - Eğer eksikse (özellikle bazı Linux dağıtımlarında), Python’ın Tk desteğini ayrıca yüklemeniz gerekebilir. macOS ve Windows’ta genellikle varsayılan olarak mevcuttur.

## Model Kurulumu

- Ollama ile çalıştırmak istediğiniz modeli (örneğin **`llama3.2:latest`**) önceden indirmelisiniz:  
  ```bash
  ollama pull llama3.2:latest
  ```
- İndirme tamamlandıktan sonra, `ollama list` komutuyla kurulu modelleri görebilirsiniz.

## Nasıl Çalıştırılır?

1. **Bu Reposu Klonlayın veya İndirin**  
   ```bash
   git clone https://github.com/KullaniciAdiniz/Cenker_llma_UI.git
   cd Cenker_llma_UI
   ```

2. **(İsteğe Bağlı) Sanal Ortam Oluşturma**  
   Kendi bağımlılıklarınızı izole etmek için (önerilir, ama zorunlu değil):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # .\venv\Scripts\activate  # Windows
   ```

3. **Gerekli Paketleri Kurun**  
   ```bash
   pip install ollama
   ```
   (Python 3.9+ ortamı kullandığınızdan emin olun.)

4. **Uygulamayı Çalıştırın**  
   ```bash
   python3 Cenker_llma_UI.py
   ```
   Ardından bir Tkinter penceresi açılacak. Metninizi girip “Gönder” (Send) butonuna basarak sohbet etmeye başlayabilirsiniz.

## Kullanım

1. **Prompt Girişi**: Metin kutusuna mesajınızı yazın.  
2. **Gönder Butonu**: Tıklayın, uygulama Ollama üzerinden modeli çağırarak yanıt üretmeye çalışır.  
3. **Cevap Görüntüleme**: Asistan (model) yanıtı, sohbet ekranında “Assistant:” başlığı altında gösterilir.  
4. **Bağlam Koruma**: Kod içinde “conversation_history” adlı bir liste, önceki mesajların prompt’a yeniden eklenmesini sağlar. Uzun sohbetlerde veya çok fazla mesaj birikiminde performans düşebilir. Gerekirse “windowing” veya geçmişi kısaltma yöntemleri uygulayabilirsiniz.

## Sık Karşılaşılan Sorunlar

- **Model Adı ile İlgili Hatalar**:  
  - Kod içinde `generate(model="llama3.2:latest", ...)` geçiyor ancak sizde “llama3.2:latest” yoksa önce `ollama pull llama3.2:latest` komutuyla indirin veya `model` parametresini elinizdeki modele göre değiştirebilirsiniz.
- **Yanıt Gelmeme Durumu**:  
  - Uzun yükleme süreleri, yetersiz bellek (RAM) veya CPU/GPU kaynakları soruna yol açabilir.  
  - Terminalde `ollama run llama3.2:latest "Hello"` komutunu deneyerek modelin tek başına çalıştığından emin olun.  
- **KeyError: 'data'** veya `'response'`**:  
  - Ollama’nın farklı sürümlerinde chunk formatı tuple/dict olarak değişebiliyor. Bu script, `"data"` ve `"response"` anahtarlarını yakalayarak yanıt biriktirir.
