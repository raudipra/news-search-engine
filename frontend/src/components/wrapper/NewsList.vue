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
      default: () => [
        {
          "source": {
            "id": "techcrunch",
            "name": "TechCrunch"
          },
          "author": "Catherine Shu",
          "title": "Early-stage venture firm The Fund launches in Australia",
          "description": "The Fund, the early-stage investment firm focused on pre-seed and seed startups, is going Down Under for its latest expansion. The Fund was founded in New York in 2018, before launching in Los Angeles, London, the Rockies and the Midwest, too. Co-founder Jenn…",
          "url": "http://techcrunch.com/2021/06/15/early-stage-venture-firm-the-fund-launches-in-australia/",
          "urlToImage": "https://techcrunch.com/wp-content/uploads/2021/06/5130649.jpg?w=533",
          "publishedAt": "2021-06-16T02:19:52Z",
          "content": "The Fund Australias team (l to r): Elicia McDonald, Adrian Petersen, Georgia Vidler, Ed Taylor and Todd Deacon\r\nThe Fund, the early-stage investment firm focused on pre-seed and seed startups, is goi… [+4187 chars]"
        },
        {
          "source": {
            "id": "techcrunch",
            "name": "TechCrunch"
          },
          "author": "Catherine Shu",
          "title": "Early-stage venture firm The Fund launches in Australia",
          "description": "The Fund, the early-stage investment firm focused on pre-seed and seed startups, is going Down Under for its latest expansion.  The Fund was founded in New...",
          "url": "https://techcrunch.com/2021/06/15/early-stage-venture-firm-the-fund-launches-in-australia/",
          "urlToImage": "https://s.yimg.com/ny/api/res/1.2/UNxcuOa6ZfP3F0r41q2yzQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTIwMDA7aD0xNTAw/https://s.yimg.com/uu/api/res/1.2/7DtH5buDFhTB9SdOvbC.Ag--~B/aD0zNTk4O3c9NDc5NzthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/techcrunch_350/07a5607a38a166f414f312c88e9d939d",
          "publishedAt": "2021-06-16T02:19:52Z",
          "content": "A group photo of The Fund Australias team (left to right): Elicia McDonald, Adrian Petersen, Georgia Vidler, Ed Taylor and Todd Deacon\r\nThe Fund Australias team (l to r): Elicia McDonald, Adrian Pete… [+4323 chars]"
        }
      ]
    }
  }
}
</script>
