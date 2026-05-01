<template>
  <section id="noticias" class="py-20 px-8 max-w-7xl mx-auto">
    <div class="flex justify-between items-end mb-12">
      <div>
        <span class="text-secondary font-label-md text-label-md uppercase tracking-widest">Actualidad</span>
        <h2 class="font-h2 text-h2 text-primary mt-2">Noticias y Eventos</h2>
      </div>
    </div>

    <div v-if="loading" class="flex justify-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
    </div>

    <div v-else-if="error" class="text-center py-12 text-error">
      <p>{{ error }}</p>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <article v-for="(news, index) in newsList" :key="index" class="bg-surface-container-lowest rounded-xl overflow-hidden shadow-[0px_4px_20px_rgba(0,0,0,0.05)] hover:shadow-[0px_8px_30px_rgba(0,0,0,0.08)] transition-all group">
        <div class="h-48 overflow-hidden relative">
          <img :src="news.image" :alt="news.title" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" loading="lazy">
        </div>
        <div class="p-6">
          <div class="flex items-center gap-2 text-slate-500 text-caption font-caption mb-3">
            <span class="material-symbols-outlined text-[16px]">calendar_today</span>
            {{ formatDate(news.date) }}
          </div>
          <h3 class="font-h3 text-h3 text-primary mb-3 line-clamp-2">{{ news.title }}</h3>
          <p class="text-on-surface-variant font-body-md text-body-md line-clamp-2 mb-4">{{ news.summary }}</p>
          <a :href="news.link" target="_blank" class="text-primary font-semibold flex items-center gap-1 hover:underline text-sm">
            Leer más <span class="material-symbols-outlined text-xs">chevron_right</span>
          </a>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const newsList = ref([])
const loading = ref(true)
const error = ref(null)

const formatDate = (dateString) => {
  try {
    return new Date(dateString).toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' })
  } catch (e) {
    return dateString
  }
}

onMounted(async () => {
  try {
    // Calling Django Backend API
    const baseUrl = 'https://sitio-web-curumani.onrender.com'
    const response = await axios.get(`${baseUrl}/api/news/`)
    if (response.data && response.data.articles) {
      newsList.value = response.data.articles
    }
  } catch (err) {
    console.error('Error fetching news:', err)
    error.value = 'No se pudieron cargar las noticias en este momento.'
  } finally {
    loading.value = false
  }
})
</script>
