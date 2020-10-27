<template>
    <div>
        <h4>用户表单</h4>
        <el-table
            :data="users"
            border
            style="width: 42%">
            <el-table-column
                fixed
                prop="id"
                label="ID"
                width="150">
            </el-table-column>
            <el-table-column
                prop="username"
                label="姓名"
                width="120">
            </el-table-column>
            <el-table-column
                prop="age"
                label="年龄"
                width="120">
            </el-table-column>
            <el-table-column
                prop="content"
                label="个人信息"
                width="120">
            </el-table-column>
            <el-table-column
                fixed="right"
                label="操作"
                width="100">
                <template slot-scope="scope">
                    <el-button @click="del_user(index)" type="text" size="small">删除</el-button>
                    <el-button type="text" size="small" @click="looking(scope.row)">查看</el-button>
<!--                    <router-link :to="`/detail/${user.id}/${user.username}/${user.age}`">查看</router-link>-->
                </template>
            </el-table-column>
        </el-table>

        <hr>

        <tr>
            <td>用户名：</td>
            <td><el-input size="small" placeholder="请输入内容" suffix-icon="el-icon-date" style="width: auto" v-model="username"></el-input></td>
        </tr>
        <tr>
            <td>年龄：</td>
            <td><el-input size="small" placeholder="请输入内容" suffix-icon="el-icon-date" style="width: auto" v-model="age"></el-input></td>
        </tr>
        <tr>
            <td>个人信息：</td>
            <td><el-input size="small" placeholder="请输入内容" suffix-icon="el-icon-date" style="width: auto" v-model="content"></el-input></td>
        </tr>
        <tr>
            <td>
                <el-button type="success" round @click="add_user">添加用户</el-button>
            </td>
        </tr>
    </div>
</template>

<script>
export default {
    name: "User",
    data() {
        return {
            users: localStorage.users ? JSON.parse(localStorage.users) : [],
            username: '',
            age: '',
            content: '',
        }
    },
    methods: {
        add_user() {
            if (this.username!==''&&this.age!==''&&this.content!==''){
                if (!this.users.length) {
                    let user = {'id': 1, username: this.username, age: this.age, content: this.content};
                    this.users.push(user);
                    localStorage.users = JSON.stringify(this.users);
                    this.username = '';
                    this.age = '';
                    this.content = '';
                }
                else {
                    let user = {'id': this.users[this.users.length-1].id + 1, username: this.username, age: this.age, content: this.content};
                    this.users.push(user);
                    localStorage.users = JSON.stringify(this.users);
                    this.username = '';
                    this.age = '';
                    this.content = '';
                }
            }
        },
        looking(row) {
            this.$router.push({path: '/detail/'+ row.id + '/' + row.username + '/' + row.age})
        },
        del_user(index) {
            this.users.splice(index, 1);
            localStorage.users = JSON.stringify(this.users);
            if (!this.users.length){
                localStorage.removeItem("users");
            }
        }
    },
}
</script>

<style scoped>

</style>
