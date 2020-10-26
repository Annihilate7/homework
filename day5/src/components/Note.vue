<template>
    <div>
        <h4>留言板</h4>
        <el-input size="small" placeholder="请输入内容" suffix-icon="el-icon-date" style="width: auto" v-model="note"></el-input>

        <el-button type="success" round @click="addNote">添加留言</el-button>

        <ul>
            <li v-for="(note, index) in notes" :key="index">
                <span>{{note}}</span>
                <el-button type="danger" icon="el-icon-delete" circle @click="remove(index)"></el-button>
            </li>
        </ul>

        <span>留言总数量：{{notes.length}}条</span>
        <br><br>
        <el-button type="danger" round v-show="flag" @click="remove_all(0, notes.length)">删除所有</el-button>
    </div>
</template>

<script>
export default {
    name: "Note",
    data:function () {
        return {
            note: "",
            notes: localStorage.notes ? JSON.parse(localStorage.notes) : [],
            flag: true,
        }
    },
    methods: {
        addNote() {
            let note = this.note;
            if (note){
                this.notes.push(this.note);
                localStorage.notes = JSON.stringify(this.notes);
                this.note = "";
                this.flag = true;
            }
        },
        remove(index) {
            this.notes.splice(index, 1)
            localStorage.notes = JSON.stringify(this.notes);
            if (!this.notes.length){
                this.flag = false;
                localStorage.removeItem("notes");
            }
        },
        remove_all(index, num){
            this.notes.splice(index, num);
            localStorage.removeItem("notes");
            this.flag = false;
        }
    },
    created: function () {
        let notes = this.notes;
        if (!notes.length) {
            this.flag = false;
        }
    },
}
</script>

<style scoped>

</style>
