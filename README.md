# zelanser
<div align="center">

# 🚀 Zelanser - Freelance Web Platform

**منصة ويب متخصصة للعمل الحر موجهة للسوق العربي، مصممة هندسياً لربط العملاء والمستقلين بأمان وكفاءة عالية.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-REST%20API-red?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-blue?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-Cache-red?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-Orchestration-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

</div>

---

## 🌟 نبذة عن المشروع (About)
**Zelanser** هو نظام خلفي (Backend) متكامل لمنصة عمل حر مصممة خصيصاً لتلبية احتياجات السوق العربي. يركز المشروع على بنية برمجية قوية، إدارة آمنة للبيانات، تصميم مرن لـ RESTful APIs، ومعالجة المهام بكفاءة عالية لضمان تجربة مستخدم سلسة واحترافية.

---

## 🛠️ التقنيات والمكتبات المستخدمة (Tech Stack)

* **اللغة الأساسية:** Python 3.11+
* **إطار العمل:** Django & Django REST Framework (DRF)
* **قاعدة البيانات:** PostgreSQL
* **التخزين المؤقت وإدارة المهام (Caching & Task Queue):** Redis & Celery
* **الاختبارات (Testing):** Pytest
* **بيئة التشغيل:** Docker & Docker Compose (لإدارة الخدمات محلياً)

---

## 📁 هيكلية المشروع (Project Architecture)

* إدارة قواعد البيانات المتقدمة ونمذجة العلاقات (Database Modeling).
* نظام صلاحيات مخصص (Custom Permissions) وتوثيق آمن.
* معالجة المهام الخلفية غير المتزامنة عبر Celery و Redis.
* نظام تخزين مؤقت متكامل عبر جدول مخصص في قاعدة البيانات.

---

## 🚀 طريقة التشغيل محلياً (Local Installation Guide)

اتبع الخطوات التالية لتشغيل المشروع وإعداده على جهازك:

### 1. استنساخ المستودع (Clone)
```bash
git clone [https://github.com/Abdelaati/zelanser.git](https://github.com/Abdelaati/zelanser.git)
cd zelanser
