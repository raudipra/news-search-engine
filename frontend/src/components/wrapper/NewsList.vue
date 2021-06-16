<template>
  <div>
    <div
      v-for="(item, index) in items"
      :key="index"
      :class="['col', `q-px-sm`]"
    >
      <NewsCard
        :source="item.source.name"
        :title="item.title"
        :description="item.description"
        :url="item.url"
        :imageUrl="item.urlToImage"
      />
    </div>
  </div>
</template>

<script>
import NewsCard from 'components/card/NewsCard.vue'

export default {
  name: 'NewsList',
  components: {
    NewsCard
  },
  props: {
    items: {
      type: Array,
      default: () => []
    }
  }
}
</script>
