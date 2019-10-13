<template>
  <div>
    <v-container fluid>
      <v-row justify="space-between">
        <v-col lg="10" md="10" sm="10">
          <v-autocomplete
            v-model="selectedCats"
            :items="allCategories"
            item-text="name"
            item-value="name"
            chips
            multiple
            hide-details
            solo
            clearable
            full-width
            label="Search by category"
            prepend-inner-icon="search"
            color="grey"
          >
            <template v-slot:selection="data">
              <v-chip
                v-if="data.index < 2"
                v-bind="data.attrs"
                :input-value="data.selected"
                close
                @click="data.select"
                @click:close="remove(data.item)"
              >
                <v-avatar left>
                  <v-icon small>
                    {{ data.item.icon }}
                  </v-icon>
                </v-avatar>
                <span>{{ data.item.name }}</span>
              </v-chip>
              <!-- Change selection appearance if more than 2 categories are selected -->
              <span v-if="data.index === 2" class="grey-text caption">
                (+{{ selectedCats.length - 2 }} others)
              </span>
            </template>
            <template v-slot:item="data">
              <template v-if="typeof data.item !== 'object'">
                <v-list-item-content v-text="data.item" />
              </template>
              <template v-else>
                <v-list-item-avatar>
                  <v-icon>{{ data.item.icon }}</v-icon>
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title v-text="data.item.name" />
                  <v-list-item-subtitle v-text="data.item.subject" />
                </v-list-item-content>
              </template>
            </template>
          </v-autocomplete>
        </v-col>
        <v-col lg="2" md="2" sm="2" class="mt-1">
          <v-btn icon color="blue" @click="search">
            <v-icon>search</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
export default {
  name: 'SearchBox',
  data () {
    return {
      allCategories: [
        { header: 'Computer Science' },
        { name: 'cs.AI', subject: 'Artificial Intelligence', icon: 'face' },
        { name: 'cs.CV', subject: 'Computer Vision and Pattern Recognition', icon: 'remove_red_eye' },
        { name: 'cs.LG', subject: 'Learning', icon: 'menu_book' },
        { name: 'cs.RO', subject: 'Robotics', icon: 'android' },
        { divider: true },
        { header: 'Electrical Engineering and Systems Science' },
        { name: 'eess.AS', subject: 'Audio and Speech Processing', icon: 'volume_up' },
        { name: 'eess.IV', subject: 'Image and Video Processing', icon: 'videocam' },
        { divider: true },
        { header: 'Statistics' },
        { name: 'stat.ML', subject: 'Machine Learning', icon: 'bar_chart' }
      ],
      selectedCats: []
    }
  },
  computed: {
    ...mapState({
      categories: state => state.categories
    })
  },
  methods: {
    ...mapMutations([
      'setCategories',
      'setInfiniteLoadingFlag'
    ]),
    remove (item) {
      const index = this.selectedCats.indexOf(item.name)
      if (index >= 0) { this.selectedCats.splice(index, 1) }
    },
    search () {
      this.setCategories(this.selectedCats)
      this.setInfiniteLoadingFlag(true)
    }
  }
}
</script>

<style scoped>

</style>
