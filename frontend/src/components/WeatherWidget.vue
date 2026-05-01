<template>
  <section class="bg-[#005A8D]/5 border-y border-[#005A8D]/10 py-4">
    <div class="max-w-7xl mx-auto px-8 flex justify-between items-center flex-wrap gap-4">
      <div class="flex items-center gap-3">
        <span class="material-symbols-outlined text-[#005A8D] text-3xl">partly_cloudy_day</span>
        <div>
          <h3 class="text-sm font-bold text-[#005A8D]">Clima en Curumaní, Cesar</h3>
          <p v-if="loading" class="text-xs text-slate-500">Cargando datos del clima...</p>
          <p v-else-if="error" class="text-xs text-red-500">{{ error }}</p>
          <div v-else class="flex items-center gap-4 text-sm text-slate-700">
            <span class="font-bold text-lg">{{ weather.temp }}°C</span>
            <span class="capitalize">{{ weather.description }}</span>
            <span class="flex items-center gap-1" title="Humedad">
              <span class="material-symbols-outlined text-[16px]">humidity_percentage</span>
              {{ weather.humidity }}%
            </span>
            <span class="flex items-center gap-1" title="Viento">
              <span class="material-symbols-outlined text-[16px]">air</span>
              {{ weather.wind }} m/s
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const loading = ref(true)
const error = ref(null)
const weather = ref({
  temp: null,
  description: '',
  humidity: null,
  wind: null
})

onMounted(async () => {
  try {
    const apiKey = 'fdf80b46a236e8df6feb51196f62c4f7'
    const city = 'Curumaní,CO'
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=es`
    
    const response = await axios.get(url)
    
    if (response.data) {
      weather.value = {
        temp: Math.round(response.data.main.temp),
        description: response.data.weather[0].description,
        humidity: response.data.main.humidity,
        wind: response.data.wind.speed
      }
    }
  } catch (err) {
    console.error('Error fetching weather:', err)
    error.value = 'No se pudo cargar el clima.'
  } finally {
    loading.value = false
  }
})
</script>
