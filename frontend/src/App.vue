<script setup>
import HeroHeader from './components/HeroHeader.vue'
import WeatherWidget from './components/WeatherWidget.vue'
import NewsSection from './components/NewsSection.vue'
import DirectoryMap from './components/DirectoryMap.vue'
import CurumaniInfo from './components/CurumaniInfo.vue'
import CommunityCalendar from './components/CommunityCalendar.vue'
import FooterSection from './components/FooterSection.vue'
</script>

<template>
  <div class="bg-background font-body-md text-on-surface">
    <HeroHeader />
    <WeatherWidget />
    <NewsSection />
    <CurumaniInfo />
    <DirectoryMap />
    <CommunityCalendar />
    
    <!-- Gestión Ciudadana from code.html -->
    <section id="servicios" class="py-24 px-8 max-w-7xl mx-auto">
      <div class="text-center mb-16">
        <h2 class="font-h1 text-h1 text-primary">Gestión Ciudadana</h2>
        <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto mt-4">Accede a información sobre servicios públicos y realiza tus trámites municipales de forma ágil.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-12 max-w-5xl mx-auto">
        <a href="https://www.acuacur-curumani-cesar.gov.co/" target="_blank" class="flex flex-col items-center text-center group cursor-pointer bg-white p-6 rounded-2xl hover:shadow-xl transition-all border border-transparent hover:border-slate-100">
          <div class="w-16 h-16 rounded-full bg-[#005A8D]/10 flex items-center justify-center text-[#005A8D] mb-6 group-hover:bg-primary group-hover:text-white transition-all shadow-sm">
            <span class="material-symbols-outlined text-3xl">water_drop</span>
          </div>
          <h3 class="font-h3 text-h3 text-primary mb-3">Acuacur</h3>
          <p class="text-on-surface-variant font-body-md text-body-md">Acueducto y Alcantarillado de Curumaní. Reportes de fugas y pago de facturas en línea.</p>
          <span class="mt-4 text-sm text-secondary font-bold group-hover:underline">Ir a la página</span>
        </a>
        <a href="https://www.afinia.com.co" target="_blank" class="flex flex-col items-center text-center group cursor-pointer bg-white p-6 rounded-2xl hover:shadow-xl transition-all border border-transparent hover:border-slate-100">
          <div class="w-16 h-16 rounded-full bg-[#005A8D]/10 flex items-center justify-center text-[#005A8D] mb-6 group-hover:bg-primary group-hover:text-white transition-all shadow-sm">
            <span class="material-symbols-outlined text-3xl">lightbulb</span>
          </div>
          <h3 class="font-h3 text-h3 text-primary mb-3">Afinia</h3>
          <p class="text-on-surface-variant font-body-md text-body-md">Servicio de Energía Eléctrica. Gestión de cortes programados y facturación.</p>
          <span class="mt-4 text-sm text-secondary font-bold group-hover:underline">Ir a la página</span>
        </a>
        <a href="https://www.facebook.com/alcaldiadecurumani/?locale=es_LA" target="_blank" class="flex flex-col items-center text-center group cursor-pointer bg-white p-6 rounded-2xl hover:shadow-xl transition-all border border-transparent hover:border-slate-100">
          <div class="w-16 h-16 rounded-full bg-[#005A8D]/10 flex items-center justify-center text-[#005A8D] mb-6 group-hover:bg-primary group-hover:text-white transition-all shadow-sm">
            <span class="material-symbols-outlined text-3xl">account_balance</span>
          </div>
          <h3 class="font-h3 text-h3 text-primary mb-3">Alcaldía</h3>
          <p class="text-on-surface-variant font-body-md text-body-md">Alcaldía de Curumaní. Trámites municipales, certificados y PQRSD.</p>
          <span class="mt-4 text-sm text-secondary font-bold group-hover:underline">Ir a la página</span>
        </a>
      
      </div>
    </section>

    <FooterSection />
  </div>
</template>

<style>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}
</style>
