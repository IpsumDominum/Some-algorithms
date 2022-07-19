#include <iostream>
#include <string> // Gain access to std::string
#include <sstream>
#include <vector>
#include<bits/stdc++.h>

bool compare(std::string a,std::string b)
{
    return a<b;
}
class Leaf
{
    public:
        Leaf* parent;
        std::vector<Leaf*> children;
        std::string canonical_name = "";
        Leaf(){
            children = {};
        }
};
class RootedTree
{
    public:
        std::vector<Leaf*> nodes;
        int root_idx = 0;
        RootedTree(){
            nodes = {};
        }
};
void assign_canonical_names(Leaf* v){
    if(v->children.size()==0){
        v->canonical_name = "10";
        return;
    }else{
        std::vector<std::string> names = {};
        for(int i=0;i<v->children.size();i++){
            assign_canonical_names(v->children[i]);
            names.push_back(v->children[i]->canonical_name);
        }
        std::sort(names.begin(),names.end(),compare);
        std::string temp = "";
        for(int i=0;i<names.size();i++){
            temp += names[i];
        }
        v->canonical_name = "1"+temp+"0";
        return;
    }
}
bool is_rooted_tree_isomorphic(RootedTree* tree1,RootedTree* tree2){
    if(tree1->nodes[tree1->root_idx]->canonical_name==""){
        assign_canonical_names(tree1->nodes[tree1->root_idx]);
    }else{
        /*pass*/
    }
    if(tree2->nodes[tree2->root_idx]->canonical_name==""){
        assign_canonical_names(tree2->nodes[tree2->root_idx]);
    }else{
        /*pass*/
    }
    std::string name1 = tree1->nodes[tree1->root_idx]->canonical_name;
    std::string name2 = tree2->nodes[tree2->root_idx]->canonical_name;
    if(name1==name2){
        return true;
    }else{
        return false;
    }
}
int main(int arg, char** argv)
{
	std::string s;
    std::string buf;        
    std::string output = "";
    int num_input = 0;
    while(true){        
        std::vector<RootedTree*> rooted_trees;
        std::getline(std::cin, s);
        int num_trees = std::stoi(s);
        if(num_trees==0){
            break;
        }
        //Get All Trees        
        for(int i=0;i<num_trees;i++){
            //Get node num
            std::getline(std::cin, s);
            std::stringstream ss(s);
            ss >> buf;
            int num_nodes = std::stoi(buf);
            //Get nodes and create tree
            RootedTree* tree = new RootedTree();
            std::vector<int> connections;
            for(int j=0;j<num_nodes;j++){
                ss >> buf;
                int buf_num = std::stoi(buf);
                Leaf* leaf = new Leaf();
                tree->nodes.push_back(leaf);
                connections.push_back(buf_num);
            }
            for(int j=0;j<connections.size();j++){
                if(connections[j]!=-1){
                    tree->nodes[j]->parent = tree->nodes[connections[j]];
                    tree->nodes[connections[j]]->children.push_back(tree->nodes[j]);
                }else{
                    tree->root_idx = j;
                }
            }
            rooted_trees.push_back(tree);
        }
        //Now compare between each rooted tree.
        output += std::to_string(num_input)+": 0";
        std::vector<RootedTree*> canonical_trees = {rooted_trees[0]};        
        for(int i=1;i<num_trees;i++){
            bool found = false;
            for(int j=0;j<canonical_trees.size();j++){
                RootedTree* compare_tree = canonical_trees[j];
                if(is_rooted_tree_isomorphic(rooted_trees[i],compare_tree)){
                    output += " "+std::to_string(j);
                    found = true;
                    break;
                }
            }
            if(found==false){
                //No comparable tree
                canonical_trees.push_back(rooted_trees[i]);
                output += " "+std::to_string(canonical_trees.size()-1);
            }else{
                continue;
            }
        }
        output += "\n";
        num_input ++;
    }
    std::cout<<output;
	return 0;
}