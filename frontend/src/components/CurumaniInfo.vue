<template>
  <section id="conocer-curumani" class="py-24 px-8 bg-surface-container-lowest relative overflow-hidden">
    <!-- Decorative background elements -->
    <div class="absolute top-0 right-0 w-96 h-96 bg-[#005A8D]/5 rounded-full blur-3xl -translate-y-1/2 translate-x-1/3"></div>
    <div class="absolute bottom-0 left-0 w-64 h-64 bg-[#F39200]/5 rounded-full blur-2xl translate-y-1/3 -translate-x-1/4"></div>

    <div class="max-w-7xl mx-auto relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
        <!-- Image and visual side -->
        <div class="relative group">
          <div class="absolute inset-0 bg-gradient-to-br from-[#005A8D] to-[#F39200] rounded-3xl transform rotate-3 scale-105 opacity-20 group-hover:rotate-6 transition-transform duration-500"></div>
          <div class="relative rounded-3xl overflow-hidden shadow-2xl bg-white p-2">
            <!-- Using local image for Curumaní -->
            <img src="../assets/curumani.jpg" alt="Paisaje de Curumaní, Cesar" class="w-full h-[500px] object-cover rounded-2xl transform group-hover:scale-105 transition-transform duration-700">
            <div class="absolute bottom-6 left-6 right-6 bg-white/90 backdrop-blur-md p-4 rounded-xl shadow-lg flex items-center gap-4">
              <div class="bg-[#005A8D] w-12 h-12 rounded-full flex items-center justify-center text-white shrink-0">
                <span class="material-symbols-outlined">map</span>
              </div>
              <div>
                <p class="text-sm font-bold text-[#005A8D]">Ubicación Estratégica</p>
                <p class="text-xs text-slate-600">Corazón del departamento del Cesar</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Text and content side -->
        <div>
          <span class="text-secondary font-label-md text-label-md uppercase tracking-widest flex items-center gap-2 mb-2">
            <span class="w-8 h-[2px] bg-secondary inline-block"></span>
            Nuestra Tierra
          </span>
          <h2 class="font-h1 text-h1 text-primary mb-6">Conoce Más de <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#005A8D] to-[#F39200]">Curumaní</span></h2>
          
          <p class="text-on-surface-variant font-body-lg text-body-lg mb-8 leading-relaxed">
            Fundado el 26 de noviembre de 1579, Curumaní es un municipio vibrante y acogedor ubicado en el centro del departamento del Cesar. Conocido cariñosamente como un municipio de "puertas abiertas", destaca por la calidez de su gente y su rica herencia cultural.
          </p>

          <div class="space-y-6">
            <div class="flex gap-4">
              <div class="w-12 h-12 rounded-full bg-[#005A8D]/10 flex items-center justify-center text-[#005A8D] shrink-0 mt-1">
                <span class="material-symbols-outlined">agriculture</span>
              </div>
              <div>
                <h3 class="font-h3 text-h3 text-primary mb-2">Riqueza Agrícola</h3>
                <p class="text-on-surface-variant font-body-md text-body-md">Nuestra economía se impulsa gracias a la ganadería y la agricultura. Somos productores destacados de maíz, yuca, frijol, plátano y cítricos, aprovechando nuestras fértiles tierras.</p>
              </div>
            </div>

            <div class="flex gap-4">
              <div class="w-12 h-12 rounded-full bg-[#005A8D]/10 flex items-center justify-center text-[#005A8D] shrink-0 mt-1">
                <span class="material-symbols-outlined">festival</span>
              </div>
              <div>
                <h3 class="font-h3 text-h3 text-primary mb-2">Cultura y Tradición</h3>
                <p class="text-on-surface-variant font-body-md text-body-md">Nuestras festividades son un derroche de alegría. Celebramos con orgullo las fiestas de la Virgen del Carmen y nuestro tradicional Festival Folclórico y Cultural.</p>
              </div>
            </div>

            <div class="flex gap-4">
              <div class="w-12 h-12 rounded-full bg-[#005A8D]/10 flex items-center justify-center text-[#005A8D] shrink-0 mt-1">
                <span class="material-symbols-outlined">landscape</span>
              </div>
              <div>
                <h3 class="font-h3 text-h3 text-primary mb-2">Belleza Natural</h3>
                <p class="text-on-surface-variant font-body-md text-body-md">Rodeados por la majestuosa Serranía del Perijá y bañados por las aguas de la ciénaga de Zapatosa, ofrecemos paisajes únicos y una biodiversidad envidiable.</p>
              </div>
            </div>
          </div>

     
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// Info section for Curumaní
</script>
