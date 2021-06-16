<template>
  <q-card v-ripple class="news-card q-mt-sm q-mb-sm" flat bordered>
    <q-card-section horizontal>
      <q-card-section class="col-8 q-pt-xs">
        <div class="text-overline">{{ source }}</div>
        <div v-on:click="openLink" class="text-h5 cursor-pointer q-hoverable q-mt-sm q-mb-xs">{{ title }}</div>
        <div class="text-caption text-grey">
          {{ description }}
        </div>
      </q-card-section>

      <q-card-section class="col-4 flex flex-center">
        <img
          height=200px
          class="rounded-borders"
          :src="imageUrl"
        />
      </q-card-section>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: 'NewsCard',
  props: {
    source: {
      type: String,
      default: ''
    },
    title: {
      type: String,
      default: ''
    },
    description: {
      type: String,
      default: ''
    },
    url: {
      type: String,
      default: ''
    },
    imageUrl: {
      type: String,
      default: ''
    }
  },
  methods: {
    openLink () {
      window.open(this.url, '_newtab')
    }
  }
}
</script>

<style lang="sass" scoped>
.news-card
  width: 100%
  max-width: 1280px
</style>
