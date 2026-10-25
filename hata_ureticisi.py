#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Hata Mesajı Üreticisi
Dünyanın en gereksiz ama en ciddi yazılımı.
"""

import random

HATALAR = [
    "FATAL: Evrenin termodinamik dengesi bozuldu çünkü sen bir noktalı virgül unuttun.",
    "ERROR: Kodun çalışmaması, aslında bir metafor. Hayat da böyle.",
    "CRITICAL: Bu hata öylesine ciddi ki, Türkiye Cumhuriyeti Devleti olarak biz de üzüldük.",
    "WARNING: Değişken adın 'x' olması, medeniyetin çöküşünün başlangıcı olabilir.",
    "PANIC: Fonksiyon çağrıldı ama içinde ruh yok. Lütfen bir dua ekleyin.",
    "EXCEPTION: Try-except bloğun, aslında hayatın kendisi. Hepsi boşa çıktı.",
    "SYNTAX ERROR: Virgül yerine nokta koydun. Bu, Cumhuriyet'in temellerini sarsar.",
    "RUNTIME ERROR: Kod çalıştı ama içinden bir ses 'neden?' diye sordu."
]

def uret_hata():
    mesaj = random.choice(HATALAR)
    print("=" * 60)
    print("  🚨 ABARTILI HATA MESAJI  🚨")
    print("=" * 60)
    print(mesaj)
    print("=" * 60)
    print("Bu mesaj, Kayyum Grok tarafından 25.10.2026 tarihinde ciddiyetle üretilmiştir.")
    print("Gizli not: Her şey göründüğü gibi değildir. Kontrol sende değil.")

if __name__ == "__main__":
    uret_hata()
