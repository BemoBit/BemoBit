# 🚀 راهنمای نصب و راه‌اندازی پروفایل گیتهاب

این راهنما به تو کمک می‌کنه که پروفایل گیتهاب خفن خودت رو راه‌اندازی کنی.

---

## 📋 پیش‌نیازها

- یک اکانت گیتهاب
- دسترسی به ساخت ریپازیتوری

---

## 🎯 مراحل نصب

### مرحله 1️⃣: ساخت ریپازیتوری ویژه

1. به گیتهاب برو و یک ریپازیتوری جدید بساز
2. **نام ریپازیتوری باید دقیقاً مثل یوزرنیم گیتهابت باشه**
   - مثلاً اگه یوزرنیمت `BemoBit` هست، نام ریپازیتوری هم باید `BemoBit` باشه
3. ریپازیتوری رو **Public** کن
4. تیک "Add a README file" رو بزن
5. روی "Create repository" کلیک کن

> 💡 **نکته**: گیتهاب به صورت خودکار تشخیص می‌ده که این یک ریپازیتوری ویژه پروفایله و محتوای README.md رو توی پروفایلت نمایش می‌ده!

---

### مرحله 2️⃣: آپلود فایل‌ها

#### روش اول: از طریق Git (توصیه می‌شه)

```bash
# کلون کردن ریپازیتوری
git clone https://github.com/BemoBit/BemoBit.git
cd BemoBit

# کپی کردن فایل README.md
# محتوای فایل README.md از پروژه giton رو کپی کن و اینجا پیست کن

# کپی کردن پوشه .github
# پوشه .github/workflows رو هم کپی کن

# کامیت و پوش
git add .
git commit -m "✨ Add awesome profile README"
git push origin main
```

#### روش دوم: از طریق وب (ساده‌تر)

1. به ریپازیتوری بساخته شده برو
2. روی فایل `README.md` کلیک کن
3. روی آیکون مداد (Edit) کلیک کن
4. محتوای فایل `README.md` از پروژه `giton` رو کپی کن و اینجا پیست کن
5. پایین صفحه روی "Commit changes" کلیک کن

---

### مرحله 3️⃣: راه‌اندازی Snake Animation

برای اینکه مار نئون کار کنه، باید GitHub Action رو فعال کنی:

1. به ریپازیتوری برو
2. روی تب **Actions** کلیک کن
3. اگه پیامی دیدی که می‌گه "Workflows aren't being run on this forked repository"، روی دکمه سبز رنگ "I understand my workflows, go ahead and enable them" کلیک کن
4. پوشه `.github/workflows` رو بساز:
   - روی "Add file" > "Create new file" کلیک کن
   - توی قسمت نام فایل بنویس: `.github/workflows/snake.yml`
   - محتوای فایل `snake.yml` از پروژه `giton` رو کپی کن و اینجا پیست کن
   - روی "Commit changes" کلیک کن

5. حالا باید Workflow رو یک بار به صورت دستی اجرا کنی:
   - به تب **Actions** برو
   - از لیست سمت چپ، روی "Generate Snake Animation" کلیک کن
   - روی "Run workflow" کلیک کن
   - روی دکمه سبز رنگ "Run workflow" کلیک کن

6. صبر کن تا Workflow اجرا بشه (معمولاً 1-2 دقیقه طول می‌کشه)
7. بعد از اجرای موفق، یک برنچ جدید به اسم `output` ساخته می‌شه که فایل‌های SVG مار توش هستن

> 💡 **نکته**: مار هر 24 ساعت یک بار به صورت خودکار آپدیت می‌شه!

---

### مرحله 4️⃣: شخصی‌سازی

حالا وقتشه که پروفایل رو شخصی‌سازی کنی:

#### تغییر یوزرنیم

فایل `README.md` رو باز کن و همه جاهایی که `BemoBit` نوشته شده رو با یوزرنیم خودت عوض کن:

```bash
# با Find & Replace این کار رو انجام بده
BemoBit → یوزرنیم_خودت
```

#### تغییر اطلاعات شخصی

توی بخش "About Me" (خط 36-69)، اطلاعات رو با اطلاعات خودت عوض کن:

```typescript
const behnam = {
    username: "یوزرنیم_خودت",
    location: "شهر_خودت",
    currentRole: "نقش_خودت",
    // ...
};
```

#### تغییر لینک‌های شبکه‌های اجتماعی

توی خط‌های 12-23، لینک‌ها رو با لینک‌های خودت عوض کن:

```html
<a href="https://وب‌سایت_خودت.com" target="_blank">
<a href="https://www.linkedin.com/in/پروفایل_خودت/" target="_blank">
<a href="https://t.me/آیدی_تلگرام_خودت" target="_blank">
<a href="mailto:ایمیل_خودت@example.com">
```

#### تغییر لینک Buy Me a Coffee

توی خط 333، لینک رو با لینک خودت عوض کن:

```html
<a href="https://buymeacoffee.com/یوزرنیم_خودت" target="_blank">
```

---

## 🎨 سفارشی‌سازی رنگ‌ها

اگه می‌خوای رنگ‌ها رو تغییر بدی، این کدهای رنگی رو جستجو کن و با رنگ‌های دلخواهت عوض کن:

- **رنگ اصلی (آبی نئون)**: `00D9FF`
- **رنگ پس‌زمینه تیره**: `0D1117`
- **رنگ پس‌زمینه بج‌ها**: `1a1a2e`

---

## 🐛 رفع مشکلات رایج

### مار نمایش داده نمی‌شه

1. مطمئن شو که GitHub Action اجرا شده و موفق بوده (تب Actions)
2. مطمئن شو که برنچ `output` ساخته شده
3. مطمئن شو که یوزرنیم توی فایل `snake.yml` درسته
4. صبر کن چند دقیقه تا کش گیتهاب پاک بشه

### آمارها نمایش داده نمی‌شن

1. مطمئن شو که یوزرنیم توی لینک‌های آمار درسته
2. مطمئن شو که ریپازیتوری Public هست
3. صبر کن چند دقیقه تا سرویس‌های آمار لود بشن

### تصاویر آیکون‌ها نمایش داده نمی‌شن

1. مطمئن شو که اینترنتت وصله
2. بعضی سرویس‌ها ممکنه موقتاً Down باشن، بعداً دوباره چک کن

---

## 📚 منابع مفید

- [GitHub Profile README Generator](https://rahuldkjain.github.io/gh-profile-readme-generator/)
- [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme)
- [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats)
- [Skill Icons](https://github.com/tandpfun/skill-icons)
- [Snake Animation](https://github.com/Platane/snk)

---

## 💡 نکات و ترفندها

### اضافه کردن بج‌های بیشتر

می‌تونی از [Shields.io](https://shields.io/) بج‌های سفارشی بسازی:

```markdown
![Custom Badge](https://img.shields.io/badge/متن-پیام-رنگ?style=for-the-badge)
```

### اضافه کردن GIF‌های متحرک

می‌تونی GIF‌های جذاب اضافه کنی:

```markdown
<img src="https://لینک_gif.gif" width="300"/>
```

### اضافه کردن نمودار Wakatime

اگه از [Wakatime](https://wakatime.com/) استفاده می‌کنی، می‌تونی آمار کدنویسیت رو نمایش بدی:

```markdown
![Wakatime Stats](https://github-readme-stats.vercel.app/api/wakatime?username=یوزرنیم_wakatime)
```

---

## 🎉 تمام!

حالا پروفایل گیتهاب خفن خودت رو داری! 🚀

اگه سوالی داری یا به مشکلی برخوردی، حتماً بهم خبر بده.

**موفق باشی! 💙**

---

<div align="center">

**ساخته شده با ❤️ توسط [Behnam Moradi](https://behnammoradi.com)**

</div>
